import random
from faker import Faker

fake = Faker("pt_BR")

Faker.seed(42)
random.seed(42)


def gerar_status(ativos=95):
    """
    Retorna Ativo ou Inativo conforme percentual informado.
    """
    return random.choices(
        ["Ativo", "Inativo"],
        weights=[ativos, 100 - ativos]
    )[0]


def gerar_valor(minimo, maximo):
    """
    Gera valor monetário.
    """
    return round(random.uniform(minimo, maximo), 2)


def gerar_data(inicio, fim):
    """
    Gera uma data aleatória entre duas datas.
    """
    return fake.date_between(
        start_date=inicio,
        end_date=fim
    )


def gerar_email(nome):
    nome = nome.lower().replace(" ", ".")

    dominios = [
        "gmail.com",
        "hotmail.com",
        "outlook.com",
        "empresa.com.br"
    ]

    return f"{nome}@{random.choice(dominios)}"
