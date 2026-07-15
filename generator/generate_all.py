"""Orquestra a geração sequencial das bases do FinanceFlow Analytics."""

import logging
import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
GENERATOR_DIR = BASE_DIR / "generator"
ETAPAS = (
    ("Clientes", "generate_clientes.py"),
    ("Fornecedores", "generate_fornecedores.py"),
    ("Contas a Pagar", "generate_contas_pagar.py"),
    ("Pagamentos", "generate_pagamentos.py"),
    ("Contas a Receber", "generate_contas_receber.py"),
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


def executar(nome: str, nome_arquivo: str) -> None:
    """Executa um gerador em processo separado e registra seu tempo."""
    arquivo = GENERATOR_DIR / nome_arquivo

    if not arquivo.exists():
        raise FileNotFoundError(f"Gerador não encontrado: {arquivo}")

    logger.info("=" * 70)
    logger.info("Iniciando: %s", nome)
    logger.info("=" * 70)
    inicio = time.perf_counter()

    subprocess.run(
        [sys.executable, str(arquivo)],
        cwd=BASE_DIR,
        check=True,
    )

    duracao = time.perf_counter() - inicio
    logger.info("%s concluído em %.2f segundos.", nome, duracao)


def main() -> None:
    """Executa o pipeline completo respeitando as dependências dos dados."""
    inicio_total = time.perf_counter()
    logger.info("=" * 70)
    logger.info("FINANCEFLOW ANALYTICS | PIPELINE DE GERAÇÃO DE DADOS")
    logger.info("=" * 70)

    try:
        for nome, nome_arquivo in ETAPAS:
            executar(nome, nome_arquivo)
    except (FileNotFoundError, subprocess.CalledProcessError) as erro:
        logger.error("Pipeline interrompido: %s", erro)
        sys.exit(1)

    logger.info("=" * 70)
    logger.info("PIPELINE FINALIZADO COM SUCESSO")
    duracao_total = time.perf_counter() - inicio_total
    logger.info("Tempo total: %.2f segundos.", duracao_total)
    logger.info("=" * 70)


if __name__ == "__main__":
    main()
