import pandas as pd
import random
from faker import Faker
from pathlib import Path

from utils import gerar_status

fake = Faker('pt_BR')

segmentos = [

    "Indústria",

    "Comércio",

    "Tecnologia",

    "Saúde",

    "Educação",

    "Financeiro",

    "Construção",

    "Agronegócio",

    "Serviços",

    "Governo"

]

portes = random.choices(

    ["Pequena", "Média", "Grande"],

    weights=[55, 30, 15],

    k=1

)[0]

estado = random.choices(

    ["SP", "RJ", "MG", "PR", "SC", "RS", "GO", "BA", "ES", "PE"],

    weights=[35, 20, 15, 8, 6, 5, 3, 3, 3, 2],

    k=1

)[0]

status = gerar_status(90)

clientes = []

TOTAL = 1000

for i in range(1, TOTAL + 1):

    cliente = {

        "id_cliente": i,

        "razao_social": fake.company(),

        "nome_fantasia": fake.company(),

        "cpf_cnpj": fake.cnpj(),

        "segmento": random.choice(segmentos),

        "porte": portes,

        "cidade": fake.city(),

        "estado": estado,

        "telefone": fake.phone_number(),

        "email": fake.company_email(),

        "status": status

    }

    clientes.append(cliente)

    df = pd.DataFrame(clientes)

    Path("data/raw").mkdir(parents=True, exist_ok=True)

df.to_csv(

    "data/raw/clientes.csv",

    index=False,

    encoding="utf-8-sig"

)

print("clientes.csv criado com sucesso!")

print(f"Total de {TOTAL} clientes gerados!")
