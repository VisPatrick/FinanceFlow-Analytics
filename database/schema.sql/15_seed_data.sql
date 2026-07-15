USE financeflow_analytics;

INSERT INTO departamentos
(nome_departamento, gestor, descricao)

VALUES

('Financeiro','Carlos Oliveira','Gestão financeira'),

('Comercial','Fernanda Lima','Área comercial'),

('Logística','Ricardo Souza','Operações logísticas'),

('Recursos Humanos','Juliana Martins','Gestão de pessoas'),

('Tecnologia','Marcos Silva','Infraestrutura de TI'),

('Marketing','Amanda Costa','Marketing institucional'),

('Administrativo','Paulo Santos','Administração'),

('Diretoria','Roberto Almeida','Gestão executiva');


INSERT INTO bancos
(codigo_banco,nome_banco)

VALUES

('001','Banco do Brasil'),

('033','Santander'),

('104','Caixa Econômica Federal'),

('237','Bradesco'),

('341','Itaú'),

('260','Nu Pagamentos'),

('077','Banco Inter'),

('212','Banco Original'),

('290','PagBank'),

('336','C6 Bank');

INSERT INTO formas_pagamento
(descricao)

VALUES

('PIX'),

('TED'),

('DOC'),

('Boleto'),

('Cartão Corporativo'),

('Transferência Bancária'),

('Dinheiro');

INSERT INTO categorias_financeiras

(nome_categoria,tipo,descricao)

VALUES

('Salários','Despesa','Folha de pagamento'),

('Encargos Trabalhistas','Despesa','INSS FGTS'),

('Energia','Despesa','Conta de energia'),

('Água','Despesa','Conta de água'),

('Internet','Despesa','Serviços de internet'),

('Telefonia','Despesa','Telefonia fixa e móvel'),

('Aluguel','Despesa','Imóveis'),

('Fretes','Despesa','Transporte'),

('Marketing','Despesa','Publicidade'),

('Materiais de Escritório','Despesa','Consumo'),

('Softwares','Despesa','Licenciamento'),

('Manutenção','Despesa','Equipamentos'),

('Serviços Terceirizados','Despesa','Prestadores'),

('Impostos','Despesa','Tributos'),

('Vendas de Produtos','Receita','Receitas'),

('Prestação de Serviços','Receita','Serviços'),

('Receitas Financeiras','Receita','Juros'),

('Outras Receitas','Receita','Diversas');

INSERT INTO centros_custo

(id_departamento,nome_centro_custo,descricao)

VALUES

(1,'Tesouraria','Controle Financeiro'),

(1,'Contas a Pagar','Pagamentos'),

(1,'Contas a Receber','Recebimentos'),

(2,'Vendas Internas','Equipe Comercial'),

(2,'Vendas Externas','Equipe Comercial'),

(3,'Distribuição','Operações'),

(3,'Armazenagem','Estoque'),

(3,'Transportes','Frota'),

(4,'Recrutamento','RH'),

(4,'Treinamento','RH'),

(5,'Infraestrutura','TI'),

(5,'Desenvolvimento','TI'),

(6,'Marketing Digital','Campanhas'),

(6,'Eventos','Eventos'),

(7,'Compras','Suprimentos'),

(7,'Administrativo Geral','Administração');