"""

Objetivo:
Gerar uma base de Contas a Pagar consistente para utilização
no ETL, Data Warehouse e Power BI.

"""

# ==========================================================
# IMPORTS
# ==========================================================

import random
import logging
from datetime import datetime, timedelta

from pathlib import Path

import pandas as pd

from mappings import (
    BANCOS,
    STATUS_CONTAS_PAGAR,
    FAIXAS_VALORES,
    SEGMENTO_CATEGORIA,
    SEGMENTO_CENTRO_CUSTO
)

# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

random.seed(42)

TOTAL_CONTAS = 15000

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"

OUTPUT_FILE = RAW_DIR / "contas_pagar.csv"

FORNECEDORES_FILE = RAW_DIR / "fornecedores.csv"

# ==========================================================
# LOGGING
# ==========================================================

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

logger = logging.getLogger(__name__)

# ==========================================================
# LEITURA DOS FORNECEDORES
# ==========================================================


def carregar_fornecedores() -> pd.DataFrame:
    """
    Carrega o CSV de fornecedores.
    """

    if not FORNECEDORES_FILE.exists():

        raise FileNotFoundError(

            f"Arquivo não encontrado:\n{FORNECEDORES_FILE}"

        )

    df = pd.read_csv(

        FORNECEDORES_FILE,

        encoding="utf-8-sig"

    )

    logger.info(

        "%s fornecedores carregados.",

        len(df)

    )

    return df

# ==========================================================
# STATUS
# ==========================================================


def gerar_status() -> str:
    """
    Gera um status conforme distribuição definida.
    """

    return random.choices(

        population=list(STATUS_CONTAS_PAGAR.keys()),

        weights=list(STATUS_CONTAS_PAGAR.values()),

        k=1

    )[0]

# ==========================================================
# BANCO
# ==========================================================


def gerar_banco() -> int:
    """
    Retorna um banco aleatório.
    """

    return random.choice(

        list(BANCOS.keys())

    )

# ==========================================================
# NOTA FISCAL
# ==========================================================


def gerar_nota_fiscal(numero: int) -> str:

    return f"NF{numero:08d}"

# ==========================================================
# OBSERVAÇÃO
# ==========================================================


def gerar_observacao(status: str) -> str:

    observacoes = {

        "Paga": [

            "Pagamento realizado com sucesso.",

            "Pagamento conciliado.",

            "Quitação confirmada."

        ],

        "Pendente": [

            "Aguardando aprovação.",

            "Aguardando pagamento.",

            "Programado para pagamento."

        ],

        "Vencida": [

            "Pagamento em atraso.",

            "Necessita regularização.",

            "Fornecedor notificou atraso."

        ],

        "Cancelada": [

            "Documento cancelado.",

            "Pagamento não autorizado.",

            "Lançamento cancelado."

        ]

    }

    return random.choice(

        observacoes[status]

    )

# ==========================================================
# VALORES
# ==========================================================


def gerar_valor() -> float:
    """
    Gera um valor financeiro conforme as faixas definidas
    em mappings.py.
    """

    faixa = random.choices(
        population=FAIXAS_VALORES,
        weights=[f[2] for f in FAIXAS_VALORES],
        k=1
    )[0]

    minimo, maximo, _ = faixa

    return round(random.uniform(minimo, maximo), 2)


# ==========================================================
# DATAS
# ==========================================================

def gerar_datas(status: str) -> tuple[datetime, datetime]:
    """Gera datas de emissão e vencimento coerentes com o status da conta."""

    hoje = datetime.today()

    if status == "Paga":
        data_vencimento = hoje - timedelta(days=random.randint(0, 670))
    elif status == "Vencida":
        data_vencimento = hoje - timedelta(days=random.randint(1, 670))
    elif status == "Pendente":
        data_vencimento = hoje + timedelta(days=random.randint(0, 60))
    else:
        data_vencimento = hoje - timedelta(days=random.randint(0, 670))

    data_emissao = data_vencimento - timedelta(days=random.randint(7, 60))
    return data_emissao, data_vencimento


# ==========================================================
# CATEGORIA
# ==========================================================

def obter_categoria(segmento: str) -> int:
    """
    Retorna o ID da categoria financeira.
    """

    return SEGMENTO_CATEGORIA[segmento]


# ==========================================================
# CENTRO DE CUSTO
# ==========================================================

def obter_centro_custo(segmento: str) -> int:
    """
    Retorna o ID do centro de custo.
    """

    return SEGMENTO_CENTRO_CUSTO[segmento]


# ==========================================================
# VALIDAÇÃO DAS DATAS
# ==========================================================

def validar_datas(
    emissao,
    vencimento
):
    """
    Garante consistência cronológica.
    """

    if vencimento < emissao:
        return False

    return True

# ==========================================================
# GERAÇÃO DAS CONTAS A PAGAR
# ==========================================================


def gerar_contas() -> pd.DataFrame:
    """
    Gera a base de Contas a Pagar.
    """

    logger.info("Iniciando geração das Contas a Pagar...")

    fornecedores = carregar_fornecedores()

    contas = []

    for i in range(1, TOTAL_CONTAS + 1):

        # ---------------------------------------------------
        # Seleciona um fornecedor aleatório
        # ---------------------------------------------------

        fornecedor = fornecedores.sample(1).iloc[0]

        id_fornecedor = int(fornecedor["id_fornecedor"])

        segmento = fornecedor["segmento"]

        categoria = obter_categoria(segmento)

        centro_custo = obter_centro_custo(segmento)

        # ---------------------------------------------------
        # Dados financeiros
        # ---------------------------------------------------

        banco = gerar_banco()

        status = gerar_status()

        valor = gerar_valor()

        # ---------------------------------------------------
        # Datas
        # ---------------------------------------------------

        data_emissao, data_vencimento = gerar_datas(status)

        # ---------------------------------------------------
        # Segurança das datas
        # ---------------------------------------------------

        if not validar_datas(
            data_emissao,
            data_vencimento
        ):
            continue

        # ---------------------------------------------------
        # Registro
        # ---------------------------------------------------

        data_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conta = {

            "id_conta": i,

            "id_fornecedor": id_fornecedor,

            "id_categoria": categoria,

            "id_centro_custo": centro_custo,

            "id_banco": banco,

            "numero_nf":
                gerar_nota_fiscal(i),

            "data_emissao":
                data_emissao.strftime("%Y-%m-%d"),

            "data_vencimento":
                data_vencimento.strftime("%Y-%m-%d"),

            "valor":
                valor,

            "status":
                status,

            "observacoes":
                gerar_observacao(status),

            "created_at": data_registro,

            "updated_at": data_registro

        }

        contas.append(conta)

        # ---------------------------------------------------
        # Log de progresso
        # ---------------------------------------------------

        if i % 1000 == 0:

            logger.info(
                "%s contas geradas...",
                i
            )

    logger.info(
        "%s contas geradas com sucesso.",
        len(contas)
    )

    return pd.DataFrame(contas)

# ==========================================================
# EXPORTAÇÃO
# ==========================================================


def salvar_csv(df: pd.DataFrame) -> None:
    """
    Salva o DataFrame em CSV.
    """

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig"
    )

    logger.info(
        "Arquivo salvo em:\n%s",
        OUTPUT_FILE.resolve()
    )


# ==========================================================
# ESTATÍSTICAS
# ==========================================================

def mostrar_estatisticas(df: pd.DataFrame) -> None:
    """
    Exibe estatísticas da base gerada.
    """

    print("\n" + "=" * 70)
    print("RESUMO DA GERAÇÃO - CONTAS A PAGAR")
    print("=" * 70)

    print(f"\nTotal de registros: {len(df):,}")

    print("\nStatus:")

    print(
        df["status"]
        .value_counts()
        .to_string()
    )

    print("\nValor total das contas:")

    print(
        f"R$ {df['valor'].sum():,.2f}"
    )

    print("\nTop 10 categorias:")

    print(
        df["id_categoria"]
        .value_counts()
        .head(10)
        .to_string()
    )

    print("\nTop 10 Bancos:")

    print(
        df["id_banco"]
        .value_counts()
        .to_string()
    )

    print("\nArquivo:")

    print(
        OUTPUT_FILE.resolve()
    )

    print("=" * 70)


# ==========================================================
# VALIDAÇÕES
# ==========================================================

def validar_dataframe(df: pd.DataFrame) -> None:
    """
    Executa validações básicas.
    """

    if df.empty:
        raise ValueError(
            "Nenhuma conta foi gerada."
        )

    if df["id_conta"].duplicated().any():

        raise ValueError(
            "IDs duplicados encontrados."
        )

    if df["numero_nf"].duplicated().any():

        raise ValueError(
            "Notas fiscais duplicadas."
        )

    if (df["valor"] <= 0).any():

        raise ValueError(
            "Existem valores negativos."
        )

    logger.info(
        "Validação concluída com sucesso."
    )


# ==========================================================
# EXPORTAÇÃO FINAL
# ==========================================================

def finalizar_geracao(df: pd.DataFrame) -> None:
    """
    Executa todas as etapas finais.
    """

    validar_dataframe(df)

    mostrar_estatisticas(df)

    salvar_csv(df)
    logger.info(
        "Geração concluída com sucesso."
    )
# ==========================================================
# MAIN
# ==========================================================


def main() -> None:
    """
    Função principal responsável pela execução do gerador.
    """

    logger.info("=" * 70)
    logger.info("FINANCEFLOW ANALYTICS")
    logger.info("Gerador de Contas a Pagar")
    logger.info("=" * 70)

    try:

        # Geração dos dados
        df = gerar_contas()

        # Finalização
        finalizar_geracao(df)

        logger.info("")
        logger.info("=" * 70)
        logger.info("PROCESSO FINALIZADO COM SUCESSO")
        logger.info("=" * 70)

    except FileNotFoundError as erro:

        logger.error("Arquivo não encontrado.")
        logger.error(erro)

    except ValueError as erro:

        logger.error("Erro de validação.")
        logger.error(erro)

    except Exception as erro:

        logger.exception("Erro inesperado.")
        logger.exception(erro)


# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == "__main__":

    main()
