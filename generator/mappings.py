"""
Mapeamentos das tabelas de domínio do banco de dados.
Todos os geradores utilizam este arquivo.

"""

# =========================================================
# BANCOS
# (IDs conforme tabela bancos)
# =========================================================

BANCOS = {
    1: "Banco do Brasil",
    2: "Santander",
    3: "Caixa Econômica Federal",
    4: "Bradesco",
    5: "Itaú",
    6: "Nu Pagamentos",
    7: "Banco Inter",
    8: "Banco Original",
    9: "PagBank",
    10: "C6 Bank"
}

# =========================================================
# FORMAS DE PAGAMENTO
# =========================================================

FORMAS_PAGAMENTO = {
    1: "PIX",
    2: "TED",
    3: "DOC",
    4: "Boleto",
    5: "Cartão Corporativo",
    6: "Transferência Bancária",
    7: "Dinheiro"
}

# =========================================================
# CATEGORIAS FINANCEIRAS
# (IDs devem ser iguais aos INSERTs do banco)
# =========================================================

CATEGORIAS = {

    1: "Salários",
    2: "Encargos Trabalhistas",
    3: "Energia",
    4: "Água",
    5: "Internet",
    6: "Telefonia",
    7: "Aluguel",
    8: "Fretes",
    9: "Marketing",
    10: "Materiais de Escritório",
    11: "Softwares",
    12: "Manutenção",
    13: "Serviços Terceirizados",
    14: "Impostos",

    15: "Vendas de Produtos",
    16: "Prestação de Serviços",
    17: "Receitas Financeiras",
    18: "Outras Receitas"

}

# =========================================================
# CENTROS DE CUSTO
# =========================================================

CENTROS_CUSTO = {

    1: "Tesouraria",
    2: "Contas a Pagar",
    3: "Contas a Receber",
    4: "Vendas Internas",
    5: "Vendas Externas",
    6: "Distribuição",
    7: "Armazenagem",
    8: "Transportes",
    9: "Recrutamento",
    10: "Treinamento",
    11: "Infraestrutura",
    12: "Desenvolvimento",
    13: "Marketing Digital",
    14: "Eventos",
    15: "Compras",
    16: "Administrativo Geral"

}

# =========================================================
# STATUS CONTAS A PAGAR
# =========================================================

STATUS_CONTAS_PAGAR = {

    "Paga": 65,
    "Pendente": 20,
    "Vencida": 10,
    "Cancelada": 5

}

# =========================================================
# STATUS CONTAS A RECEBER
# =========================================================

STATUS_CONTAS_RECEBER = {

    "Recebida": 70,
    "Pendente": 20,
    "Vencida": 8,
    "Cancelada": 2

}

# =========================================================
# DISTRIBUIÇÃO DOS VALORES
# =========================================================

FAIXAS_VALORES = [

    (100, 1000, 40),

    (1000, 5000, 35),

    (5000, 20000, 20),

    (20000, 100000, 5)

]

# =========================================================
# RELACIONAMENTO
# SEGMENTO -> CATEGORIA
# =========================================================

SEGMENTO_CATEGORIA = {

    "Tecnologia": 11,

    "Cloud": 11,

    "Telefonia": 6,

    "Energia": 3,

    "Logística": 8,

    "Transporte": 8,

    "Marketing": 9,

    "Financeiro": 17,

    "Jurídico": 13,

    "RH": 2,

    "Escritório": 10

}

# =========================================================
# RELACIONAMENTO
# SEGMENTO -> CENTRO DE CUSTO
# =========================================================

SEGMENTO_CENTRO_CUSTO = {

    "Tecnologia": 12,

    "Cloud": 11,

    "Telefonia": 11,

    "Energia": 11,

    "Logística": 6,

    "Transporte": 8,

    "Marketing": 13,

    "Financeiro": 1,

    "Jurídico": 15,

    "RH": 9,

    "Escritório": 15

}
print("Mappings carregados com sucesso.")
