USE financeflow_analytics;

-- ======================================================
-- Projeto: FinanceFlow Analytics
-- Script : 14_create_indexes.sql
-- Objetivo: Criação dos índices para otimização
-- ======================================================

/*=========================================================
FORNECEDORES
=========================================================*/

CREATE INDEX idx_fornecedor_razao_social
ON fornecedores(razao_social);

CREATE INDEX idx_fornecedor_cidade
ON fornecedores(cidade);

CREATE INDEX idx_fornecedor_estado
ON fornecedores(estado);

CREATE INDEX idx_fornecedor_status
ON fornecedores(status);


/*=========================================================
CLIENTES
=========================================================*/

CREATE INDEX idx_cliente_razao_social
ON clientes(razao_social);

CREATE INDEX idx_cliente_cidade
ON clientes(cidade);

CREATE INDEX idx_cliente_estado
ON clientes(estado);

CREATE INDEX idx_cliente_status
ON clientes(status);


/*=========================================================
CENTROS DE CUSTO
=========================================================*/

CREATE INDEX idx_cc_departamento
ON centros_custo(id_departamento);

CREATE INDEX idx_cc_nome
ON centros_custo(nome_centro_custo);


/*=========================================================
CATEGORIAS
=========================================================*/

CREATE INDEX idx_categoria_tipo
ON categorias_financeiras(tipo);

CREATE INDEX idx_categoria_nome
ON categorias_financeiras(nome_categoria);


/*=========================================================
CONTAS A PAGAR
=========================================================*/

CREATE INDEX idx_cp_fornecedor
ON contas_pagar(id_fornecedor);

CREATE INDEX idx_cp_categoria
ON contas_pagar(id_categoria);

CREATE INDEX idx_cp_centro
ON contas_pagar(id_centro_custo);

CREATE INDEX idx_cp_banco
ON contas_pagar(id_banco);

CREATE INDEX idx_cp_status
ON contas_pagar(status);

CREATE INDEX idx_cp_data_emissao
ON contas_pagar(data_emissao);

CREATE INDEX idx_cp_data_vencimento
ON contas_pagar(data_vencimento);

CREATE INDEX idx_cp_numero_nf
ON contas_pagar(numero_nf);


/*=========================================================
PAGAMENTOS
=========================================================*/

CREATE INDEX idx_pag_conta
ON pagamentos(id_conta);

CREATE INDEX idx_pag_banco
ON pagamentos(id_banco);

CREATE INDEX idx_pag_forma
ON pagamentos(id_forma_pagamento);

CREATE INDEX idx_pag_data
ON pagamentos(data_pagamento);


/*=========================================================
CONTAS A RECEBER
=========================================================*/

CREATE INDEX idx_cr_cliente
ON contas_receber(id_cliente);

CREATE INDEX idx_cr_categoria
ON contas_receber(id_categoria);

CREATE INDEX idx_cr_banco
ON contas_receber(id_banco);

CREATE INDEX idx_cr_status
ON contas_receber(status);

CREATE INDEX idx_cr_data_emissao
ON contas_receber(data_emissao);

CREATE INDEX idx_cr_data_vencimento
ON contas_receber(data_vencimento);


/*=========================================================
RECEBIMENTOS
=========================================================*/

CREATE INDEX idx_rec_conta
ON recebimentos(id_receber);

CREATE INDEX idx_rec_banco
ON recebimentos(id_banco);

CREATE INDEX idx_rec_forma
ON recebimentos(id_forma_pagamento);

CREATE INDEX idx_rec_data
ON recebimentos(data_recebimento);


/*=========================================================
FATO MOVIMENTACOES
=========================================================*/

CREATE INDEX idx_fato_data
ON fato_movimentacoes(data_movimentacao);

CREATE INDEX idx_fato_categoria
ON fato_movimentacoes(id_categoria);

CREATE INDEX idx_fato_centro
ON fato_movimentacoes(id_centro_custo);

CREATE INDEX idx_fato_banco
ON fato_movimentacoes(id_banco);

CREATE INDEX idx_fato_fornecedor
ON fato_movimentacoes(id_fornecedor);

CREATE INDEX idx_fato_cliente
ON fato_movimentacoes(id_cliente);

CREATE INDEX idx_fato_forma
ON fato_movimentacoes(id_forma_pagamento);

CREATE INDEX idx_fato_tipo
ON fato_movimentacoes(tipo_movimentacao);

CREATE INDEX idx_fato_status
ON fato_movimentacoes(status);


/*=========================================================
ÍNDICES COMPOSTOS
(Utilizados em consultas analíticas)
=========================================================*/

CREATE INDEX idx_cp_status_vencimento
ON contas_pagar(status, data_vencimento);

CREATE INDEX idx_cp_fornecedor_status
ON contas_pagar(id_fornecedor, status);

CREATE INDEX idx_cp_categoria_data
ON contas_pagar(id_categoria, data_emissao);

CREATE INDEX idx_cr_status_vencimento
ON contas_receber(status, data_vencimento);

CREATE INDEX idx_fato_data_categoria
ON fato_movimentacoes(data_movimentacao, id_categoria);

CREATE INDEX idx_fato_data_centro
ON fato_movimentacoes(data_movimentacao, id_centro_custo);

CREATE INDEX idx_fato_data_tipo
ON fato_movimentacoes(data_movimentacao, tipo_movimentacao);

CREATE INDEX idx_fato_data_banco
ON fato_movimentacoes(data_movimentacao, id_banco);