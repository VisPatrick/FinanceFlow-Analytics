"""Gera contas a receber compatíveis com a tabela ``contas_receber``."""

import logging
import random
import sys
from datetime import datetime, timedelta

import pandas as pd

from data_loader import carregar_clientes, salvar_csv
from mappings import BANCOS, FAIXAS_VALORES, STATUS_CONTAS_RECEBER

random.seed(42)

TOTAL_CONTAS = 15000
OUTPUT_FILE = "contas_receber.csv"
CATEGORIAS_RECEITA = {15: 55, 16: 30, 17: 10, 18: 5}
COLUNAS_CLIENTE_OBRIGATORIAS = {"id_cliente"}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


def carregar_base_clientes() -> pd.DataFrame:
    """Carrega e valida a base de clientes."""
    clientes = carregar_clientes()
    colunas_ausentes = COLUNAS_CLIENTE_OBRIGATORIAS.difference(
        clientes.columns
    )

    if colunas_ausentes:
        raise ValueError(
            "Colunas obrigatórias ausentes em clientes.csv: "
            f"{', '.join(sorted(colunas_ausentes))}."
        )
    if clientes.empty:
        raise ValueError("A base de clientes está vazia.")

    logger.info("%s clientes carregados.", len(clientes))
    return clientes


def gerar_categoria() -> int:
    """Retorna uma categoria de receita conforme a distribuição definida."""
    return random.choices(
        population=list(CATEGORIAS_RECEITA.keys()),
        weights=list(CATEGORIAS_RECEITA.values()),
        k=1,
    )[0]


def gerar_status() -> str:
    """Retorna um status conforme a distribuição centralizada."""
    return random.choices(
        population=list(STATUS_CONTAS_RECEBER.keys()),
        weights=list(STATUS_CONTAS_RECEBER.values()),
        k=1,
    )[0]


def gerar_datas(status: str) -> tuple[datetime, datetime]:
    """Gera datas de emissão e vencimento coerentes com o status."""
    hoje = datetime.today()

    if status == "Recebida":
        data_vencimento = hoje - timedelta(days=random.randint(0, 670))
    elif status == "Vencida":
        data_vencimento = hoje - timedelta(days=random.randint(1, 670))
    elif status == "Pendente":
        data_vencimento = hoje + timedelta(days=random.randint(0, 60))
    else:  # Cancelada
        data_vencimento = hoje - timedelta(days=random.randint(0, 670))

    data_emissao = data_vencimento - timedelta(days=random.randint(7, 60))
    return data_emissao, data_vencimento


def gerar_valor() -> float:
    """Gera um valor conforme as faixas definidas no mapeamento."""
    minimo, maximo, _ = random.choices(
        population=FAIXAS_VALORES,
        weights=[faixa[2] for faixa in FAIXAS_VALORES],
        k=1,
    )[0]
    return round(random.uniform(minimo, maximo), 2)


def gerar_observacao(status: str) -> str:
    """Gera uma observação coerente com o status da conta."""
    observacoes = {
        "Recebida": [
            "Recebimento confirmado.",
            "Valor recebido integralmente.",
            "Receita conciliada.",
        ],
        "Pendente": [
            "Aguardando pagamento.",
            "Cliente dentro do prazo.",
            "Recebimento previsto.",
        ],
        "Vencida": [
            "Cobrança em aberto.",
            "Cliente inadimplente.",
            "Necessita contato.",
        ],
        "Cancelada": [
            "Venda cancelada.",
            "Documento cancelado.",
            "Receita estornada.",
        ],
    }
    return random.choice(observacoes[status])


def gerar_contas_receber() -> pd.DataFrame:
    """Gera a base de contas a receber."""
    logger.info("Iniciando geração das contas a receber...")
    clientes = carregar_base_clientes()
    contas = []

    for i in range(1, TOTAL_CONTAS + 1):
        cliente = clientes.sample(1).iloc[0]
        status = gerar_status()
        data_emissao, data_vencimento = gerar_datas(status)
        data_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        contas.append(
            {
                "id_receber": i,
                "numero_nf": f"NF{datetime.today().year}{i:08d}",
                "id_cliente": int(cliente["id_cliente"]),
                "id_categoria": gerar_categoria(),
                "id_banco": random.choice(list(BANCOS.keys())),
                "data_emissao": data_emissao.strftime("%Y-%m-%d"),
                "data_vencimento": data_vencimento.strftime("%Y-%m-%d"),
                "valor": gerar_valor(),
                "status": status,
                "observacoes": gerar_observacao(status),
                "created_at": data_registro,
                "updated_at": data_registro,
            }
        )

        if i % 1000 == 0:
            logger.info("%s contas geradas...", i)

    df = pd.DataFrame(contas)
    logger.info("%s contas geradas com sucesso.", len(df))
    return df


def validar_dataframe(df: pd.DataFrame) -> None:
    """Executa validações de integridade da base gerada."""
    if df.empty:
        raise ValueError("Nenhuma conta a receber foi gerada.")
    if df["id_receber"].duplicated().any():
        raise ValueError("Existem IDs de contas a receber duplicados.")
    if df["numero_nf"].duplicated().any():
        raise ValueError("Existem números de nota fiscal duplicados.")
    if (df["valor"] <= 0).any():
        raise ValueError("Existem valores não positivos.")
    if not df["status"].isin(STATUS_CONTAS_RECEBER).all():
        raise ValueError("Existem status inválidos.")

    emissao = pd.to_datetime(df["data_emissao"])
    vencimento = pd.to_datetime(df["data_vencimento"])
    if (vencimento < emissao).any():
        raise ValueError("Existem vencimentos anteriores à emissão.")

    logger.info("Validação concluída com sucesso.")


def mostrar_estatisticas(df: pd.DataFrame) -> None:
    """Exibe um resumo da geração no terminal."""
    print("\n" + "=" * 70)
    print("RESUMO DA GERAÇÃO - CONTAS A RECEBER")
    print("=" * 70)
    print(f"\nTotal de registros: {len(df):,}")
    print("\nStatus:")
    print(df["status"].value_counts().to_string())
    print(f"\nValor total das contas:\nR$ {df['valor'].sum():,.2f}")
    print("\nTop 10 categorias:")
    print(df["id_categoria"].value_counts().head(10).to_string())
    print("\nBancos:")
    print(df["id_banco"].value_counts().sort_index().to_string())
    print("=" * 70)


def finalizar_geracao(df: pd.DataFrame) -> None:
    """Valida, exibe o resumo e exporta o CSV."""
    validar_dataframe(df)
    mostrar_estatisticas(df)
    salvar_csv(df, OUTPUT_FILE)
    logger.info("Arquivo %s salvo com sucesso.", OUTPUT_FILE)


def main() -> None:
    """Executa o fluxo completo do gerador."""
    try:
        finalizar_geracao(gerar_contas_receber())
    except (FileNotFoundError, ValueError) as erro:
        logger.error(erro)
        sys.exit(1)
    except Exception:
        logger.exception(
            "Erro inesperado durante a geração de contas a receber."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
