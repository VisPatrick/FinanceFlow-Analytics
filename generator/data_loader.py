"""
=========================================================
FinanceFlow Analytics

Arquivo: data_loader.py

Responsável por carregar os arquivos CSV utilizados
pelos geradores do projeto.

=========================================================
"""

from pathlib import Path

import pandas as pd

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"

# ==========================================================
# FUNÇÃO GENÉRICA
# ==========================================================


def carregar_csv(nome_arquivo: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV da pasta data/raw.

    Parameters
    ----------
    nome_arquivo : str
        Nome do arquivo.

    Returns
    -------
    pd.DataFrame
    """

    arquivo = RAW_DIR / nome_arquivo

    if not arquivo.exists():

        raise FileNotFoundError(
            f"Arquivo não encontrado:\n{arquivo}"
        )

    return pd.read_csv(
        arquivo,
        encoding="utf-8-sig"
    )

# ==========================================================
# FORNECEDORES
# ==========================================================


def carregar_fornecedores() -> pd.DataFrame:

    return carregar_csv(
        "fornecedores.csv"
    )

# ==========================================================
# CLIENTES
# ==========================================================


def carregar_clientes() -> pd.DataFrame:

    return carregar_csv(
        "clientes.csv"
    )

# ==========================================================
# CONTAS A PAGAR
# ==========================================================


def carregar_contas_pagar() -> pd.DataFrame:

    return carregar_csv(
        "contas_pagar.csv"
    )

# ==========================================================
# PAGAMENTOS
# ==========================================================


def carregar_pagamentos() -> pd.DataFrame:

    return carregar_csv(
        "pagamentos.csv"
    )

# ==========================================================
# CONTAS A RECEBER
# ==========================================================


def carregar_contas_receber() -> pd.DataFrame:

    return carregar_csv(
        "contas_receber.csv"
    )

# ==========================================================
# RECEBIMENTOS
# ==========================================================


def carregar_recebimentos() -> pd.DataFrame:

    return carregar_csv(
        "recebimentos.csv"
    )

# ==========================================================
# EXPORTAÇÃO
# ==========================================================


def salvar_csv(
    dataframe: pd.DataFrame,
    nome_arquivo: str
) -> None:
    """
    Salva um DataFrame na pasta data/raw.
    """

    RAW_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    arquivo = RAW_DIR / nome_arquivo

    dataframe.to_csv(
        arquivo,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"Arquivo salvo em:\n{arquivo.resolve()}")
