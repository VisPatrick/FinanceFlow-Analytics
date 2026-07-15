"""Configurações compartilhadas do FinanceFlow Analytics."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
EXPORT_DIR = BASE_DIR / "data" / "export"

load_dotenv(BASE_DIR / ".env")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def garantir_diretorios() -> None:
    """Cria as pastas de dados do projeto quando necessário."""
    for diretorio in (RAW_DIR, PROCESSED_DIR, EXPORT_DIR):
        diretorio.mkdir(parents=True, exist_ok=True)


def obter_configuracao_banco() -> dict[str, str | int]:
    """Retorna a configuração do MySQL e valida as variáveis obrigatórias."""
    campos_ausentes = [
        nome
        for nome, valor in {
            "DB_USER": DB_USER,
            "DB_PASSWORD": DB_PASSWORD,
            "DB_NAME": DB_NAME,
        }.items()
        if not valor
    ]

    if campos_ausentes:
        raise RuntimeError(
            "Variáveis de ambiente ausentes: "
            f"{', '.join(campos_ausentes)}. Configure o arquivo .env."
        )

    return {
        "host": DB_HOST,
        "port": DB_PORT,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "database": DB_NAME,
    }


def criar_conexao_mysql():
    """Cria uma conexão MySQL somente quando ela for solicitada."""
    try:
        import mysql.connector
    except ModuleNotFoundError as erro:
        raise RuntimeError(
            "Dependência ausente: instale 'mysql-connector-python'."
        ) from erro

    return mysql.connector.connect(**obter_configuracao_banco())
