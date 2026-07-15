"""
=========================================================
FinanceFlow Analytics
Arquivo: domain.py

Regras de negócio utilizadas pelos geradores de dados
=========================================================
"""

# =====================================================
# SEGMENTOS DOS FORNECEDORES
# =====================================================

SEGMENTOS_FORNECEDORES = {
    "Tecnologia": {
        "categoria": "Softwares",
        "portes": ["Grande", "Média"]
    },
    "Cloud": {
        "categoria": "Cloud",
        "portes": ["Grande"]
    },
    "Telefonia": {
        "categoria": "Telefonia",
        "portes": ["Grande", "Média"]
    },
    "Energia": {
        "categoria": "Energia",
        "portes": ["Grande"]
    },
    "Transporte": {
        "categoria": "Fretes",
        "portes": ["Grande", "Média", "Pequena"]
    },
    "Logística": {
        "categoria": "Fretes",
        "portes": ["Grande", "Média"]
    },
    "Marketing": {
        "categoria": "Marketing",
        "portes": ["Média", "Pequena"]
    },
    "Financeiro": {
        "categoria": "Serviços Financeiros",
        "portes": ["Grande", "Média"]
    },
    "Jurídico": {
        "categoria": "Serviços Jurídicos",
        "portes": ["Média", "Pequena"]
    },
    "RH": {
        "categoria": "Recursos Humanos",
        "portes": ["Pequena", "Média"]
    },
    "Escritório": {
        "categoria": "Materiais de Escritório",
        "portes": ["Pequena"]
    }
}

# =====================================================
# PESOS DOS SEGMENTOS
# =====================================================

PESOS_SEGMENTOS = {
    "Tecnologia": 20,
    "Logística": 15,
    "Transporte": 15,
    "Escritório": 10,
    "Cloud": 8,
    "Marketing": 8,
    "Telefonia": 7,
    "Financeiro": 5,
    "Energia": 4,
    "Jurídico": 4,
    "RH": 4
}

# =====================================================
# ESTADOS
# =====================================================

ESTADOS = [
    "SP",
    "RJ",
    "MG",
    "PR",
    "SC",
    "RS",
    "GO",
    "BA",
    "ES",
    "PE"
]

PESOS_ESTADOS = [
    35,
    20,
    15,
    8,
    6,
    5,
    3,
    3,
    3,
    2
]

# =====================================================
# PORTE DAS EMPRESAS
# =====================================================

PORTES = [
    "Pequena",
    "Média",
    "Grande"
]

PESOS_PORTES = [
    55,
    30,
    15
]

# =====================================================
# FORNECEDORES ESTRATÉGICOS
# =====================================================

FORNECEDORES_PREMIUM = [

    ("Microsoft Brasil", "Tecnologia"),
    ("Oracle Brasil", "Cloud"),
    ("Amazon AWS", "Cloud"),
    ("Google Cloud", "Cloud"),
    ("TOTVS", "Tecnologia"),
    ("Dell Technologies", "Tecnologia"),
    ("Cisco Brasil", "Tecnologia"),
    ("Intel Brasil", "Tecnologia"),
    ("Lenovo Brasil", "Tecnologia"),
    ("HP Brasil", "Tecnologia"),

    ("Claro Empresas", "Telefonia"),
    ("Vivo Empresas", "Telefonia"),
    ("TIM Empresas", "Telefonia"),

    ("JSL Logística", "Logística"),
    ("Braspress", "Transporte"),
    ("Correios", "Transporte"),
    ("Jadlog", "Transporte"),
    ("Localiza Fleet", "Transporte"),

    ("Kalunga Empresas", "Escritório"),

    ("RD Station", "Marketing"),
    ("Rock Content", "Marketing"),

    ("TOTVS Protheus", "Tecnologia"),
    ("Senior Sistemas", "Tecnologia"),
    ("Sankhya", "Tecnologia"),

    ("Stone Pagamentos", "Financeiro"),
    ("Cielo", "Financeiro"),

    ("Ultragaz", "Energia"),
    ("Neoenergia", "Energia"),
    ("Enel", "Energia"),

    ("PwC", "Financeiro"),
    ("Deloitte", "Financeiro"),
    ("KPMG", "Financeiro"),
    ("EY", "Financeiro")
]

# =====================================================
# SEGMENTOS DOS CLIENTES
# =====================================================

SEGMENTOS_CLIENTES = [
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

PESOS_SEGMENTOS_CLIENTES = [
    20,
    18,
    12,
    10,
    8,
    8,
    8,
    6,
    6,
    4
]
print("domain.py carregado com sucesso!")
