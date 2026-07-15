"""
=========================================================
FinanceFlow Analytics
Gerador de Fornecedores
=========================================================
"""

import random
from pathlib import Path

import pandas as pd
from faker import Faker

from utils import gerar_status
from domain import (
    SEGMENTOS_FORNECEDORES,
    PESOS_SEGMENTOS,
    ESTADOS,
    PESOS_ESTADOS,
    FORNECEDORES_PREMIUM
)

fake = Faker("pt_BR")

Faker.seed(42)
random.seed(42)

TOTAL_FORNECEDORES = 500


def gerar_fornecedores():

    fornecedores = []
    id_fornecedor = 1

    # ============================
    # FORNECEDORES PREMIUM
    # ============================

    for nome_empresa, segmento in FORNECEDORES_PREMIUM:

        nome_empresa_clean = (
            nome_empresa.lower()
            .replace(" ", "")
            .replace(".", " ")
        )

        fornecedor = {

            "id_fornecedor": id_fornecedor,

            "razao_social": f"{nome_empresa} LTDA",

            "nome_fantasia": nome_empresa,

            "cnpj": fake.unique.cnpj(),

            "segmento": segmento,

            "categoria_principal":
                SEGMENTOS_FORNECEDORES[segmento]["categoria"],

            "porte":
                random.choice(
                    SEGMENTOS_FORNECEDORES[segmento]["portes"]
                ),

            "cidade": fake.city(),

            "estado":
                random.choices(
                    ESTADOS,
                    weights=PESOS_ESTADOS,
                    k=1
                )[0],

            "telefone": fake.phone_number(),

            "email": f"contato@{nome_empresa_clean}.com.br",

            "status": gerar_status()

        }

        fornecedores.append(fornecedor)

        id_fornecedor += 1

    # ============================
    # FORNECEDORES FICTÍCIOS
    # ============================

    while id_fornecedor <= TOTAL_FORNECEDORES:

        segmento = random.choices(

            population=list(PESOS_SEGMENTOS.keys()),

            weights=list(PESOS_SEGMENTOS.values()),

            k=1

        )[0]

        fornecedor = {

            "id_fornecedor": id_fornecedor,

            "razao_social": fake.company(),

            "nome_fantasia": fake.company(),

            "cnpj": fake.unique.cnpj(),

            "segmento": segmento,

            "categoria_principal":
                SEGMENTOS_FORNECEDORES[segmento]["categoria"],

            "porte":
                random.choice(
                    SEGMENTOS_FORNECEDORES[segmento]["portes"]
                ),

            "cidade": fake.city(),

            "estado":
                random.choices(
                    ESTADOS,
                    weights=PESOS_ESTADOS,
                    k=1
                )[0],

            "telefone": fake.phone_number(),

            "email": fake.company_email(),

            "status": gerar_status()

        }

        fornecedores.append(fornecedor)

        id_fornecedor += 1

    # ============================
    # DATAFRAME
    # ============================

    df = pd.DataFrame(fornecedores)

    Path("../data/raw").mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        "data/raw/fornecedores.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("=" * 60)
    print("Arquivo fornecedores.csv criado com sucesso!")
    print(f"Total de fornecedores: {len(df)}")
    print("=" * 60)

    return df


if __name__ == "__main__":

    gerar_fornecedores()
print(SEGMENTOS_FORNECEDORES)
