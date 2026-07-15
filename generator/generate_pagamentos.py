"""Gera pagamentos para as contas a pagar já liquidadas."""

import logging
import random
import sys
from datetime import datetime, timedelta

import pandas as pd

from data_loader import carregar_contas_pagar, salvar_csv
from mappings import FORMAS_PAGAMENTO

random.seed(42)

OUTPUT_FILE = "pagamentos.csv"
COLUNAS_CONTA_OBRIGATORIAS = {
    "id_conta",
    "id_banco",
    "status",
    "valor",
    "data_emissao",
    "data_vencimento",
}
PESOS_FORMAS_PAGAMENTO = {
    1: 40,  # PIX
    2: 22,  # TED
    3: 2,   # DOC
    4: 10,  # Boleto
    5: 5,   # Cartão Corporativo
    6: 16,  # Transferência Bancária
    7: 5,   # Dinheiro
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


def gerar_forma_pagamento() -> int:
    """Retorna um ID de forma de pagamento conforme a distribuição definida."""
    formas = list(FORMAS_PAGAMENTO.keys())
    return random.choices(
        formas,
        weights=[PESOS_FORMAS_PAGAMENTO[forma] for forma in formas],
        k=1,
    )[0]


def carregar_pagamentos_base() -> pd.DataFrame:
    """Carrega as contas liquidadas que devem originar pagamentos."""
    contas = carregar_contas_pagar()
    colunas_ausentes = COLUNAS_CONTA_OBRIGATORIAS.difference(contas.columns)

    if colunas_ausentes:
        raise ValueError(
            "Colunas obrigatórias ausentes em contas_pagar.csv: "
            f"{', '.join(sorted(colunas_ausentes))}."
        )

    contas_pagas = contas.loc[contas["status"] == "Paga"].copy()

    if contas_pagas.empty:
        raise ValueError("Nenhuma conta com status 'Paga' foi encontrada.")

    logger.info("%s contas pagas encontradas.", len(contas_pagas))
    return contas_pagas


def gerar_dados_financeiros(conta) -> tuple[datetime, float, float, float]:
    """Calcula os valores e a data de liquidação de uma conta paga."""
    data_vencimento = pd.to_datetime(conta.data_vencimento).to_pydatetime()
    data_emissao = pd.to_datetime(conta.data_emissao).to_pydatetime()
    data_pagamento = data_vencimento + timedelta(days=random.randint(-5, 15))
    data_pagamento = min(data_pagamento, datetime.today())

    if data_pagamento < data_emissao:
        data_pagamento = data_emissao

    valor = float(conta.valor)
    dias_atraso = max((data_pagamento - data_vencimento).days, 0)
    dias_antecipacao = max((data_vencimento - data_pagamento).days, 0)
    juros = round(valor * 0.001 * dias_atraso, 2)
    desconto = round(valor * 0.0005 * dias_antecipacao, 2)
    valor_pago = round(valor + juros - desconto, 2)

    return data_pagamento, valor_pago, juros, desconto


def gerar_pagamentos() -> pd.DataFrame:
    """Gera um pagamento integral para cada conta com status ``Paga``."""
    logger.info("Iniciando geração dos pagamentos...")
    pagamentos = []

    for indice, conta in enumerate(
        carregar_pagamentos_base().itertuples(index=False), start=1
    ):
        dados_financeiros = gerar_dados_financeiros(conta)
        data_pagamento, valor_pago, juros, desconto = dados_financeiros
        data_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        pagamentos.append(
            {
                "id_pagamento": indice,
                "id_conta": int(conta.id_conta),
                "id_forma_pagamento": gerar_forma_pagamento(),
                "id_banco": int(conta.id_banco),
                "data_pagamento": data_pagamento.strftime("%Y-%m-%d"),
                "valor_pago": valor_pago,
                "juros": juros,
                "desconto": desconto,
                "created_at": data_registro,
                "updated_at": data_registro,
            }
        )

        if indice % 1000 == 0:
            logger.info("%s pagamentos gerados...", indice)

    df = pd.DataFrame(pagamentos)
    logger.info("%s pagamentos gerados com sucesso.", len(df))
    return df


def validar_dataframe(df: pd.DataFrame) -> None:
    """Valida as regras necessárias para a tabela de pagamentos."""
    if df.empty:
        raise ValueError("Nenhum pagamento foi gerado.")
    if df["id_pagamento"].duplicated().any():
        raise ValueError("Existem IDs de pagamento duplicados.")
    if df["id_conta"].duplicated().any():
        raise ValueError("Existem contas com mais de um pagamento.")
    if df["data_pagamento"].isna().any():
        raise ValueError("Existem pagamentos sem data de pagamento.")
    if (df["valor_pago"] <= 0).any():
        raise ValueError("Existem valores de pagamento não positivos.")
    if (df["juros"] < 0).any() or (df["desconto"] < 0).any():
        raise ValueError("Existem juros ou descontos negativos.")
    if not df["id_forma_pagamento"].isin(FORMAS_PAGAMENTO.keys()).all():
        raise ValueError("Existem formas de pagamento inválidas.")

    logger.info("Validação concluída com sucesso.")


def mostrar_estatisticas(df: pd.DataFrame) -> None:
    """Exibe um resumo da geração no terminal."""
    formas = df["id_forma_pagamento"].map(FORMAS_PAGAMENTO)

    print("\n" + "=" * 70)
    print("RESUMO DA GERAÇÃO - PAGAMENTOS")
    print("=" * 70)
    print(f"\nTotal de pagamentos: {len(df):,}")
    print(f"\nValor total pago:\nR$ {df['valor_pago'].sum():,.2f}")
    print("\nFormas de pagamento:")
    print(formas.value_counts().to_string())
    print("\nBancos:")
    print(df["id_banco"].value_counts().sort_index().to_string())
    print("=" * 70)


def finalizar_geracao(df: pd.DataFrame) -> None:
    """Valida, exibe o resumo e exporta os pagamentos."""
    validar_dataframe(df)
    mostrar_estatisticas(df)
    salvar_csv(df, OUTPUT_FILE)
    logger.info("Arquivo %s salvo com sucesso.", OUTPUT_FILE)


def main() -> None:
    """Executa o fluxo completo de geração de pagamentos."""
    logger.info("=" * 70)
    logger.info("FINANCEFLOW ANALYTICS | Gerador de Pagamentos")
    logger.info("=" * 70)

    try:
        finalizar_geracao(gerar_pagamentos())
    except (FileNotFoundError, ValueError) as erro:
        logger.error(erro)
        sys.exit(1)
    except Exception:
        logger.exception("Erro inesperado durante a geração de pagamentos.")
        sys.exit(1)


if __name__ == "__main__":
    main()
