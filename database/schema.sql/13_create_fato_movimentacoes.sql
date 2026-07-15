USE financeflow_analytics;

CREATE TABLE fato_movimentacoes (

    id_movimentacao BIGINT AUTO_INCREMENT PRIMARY KEY,

    id_categoria INT NOT NULL,

    id_centro_custo INT NOT NULL,

    id_banco INT NOT NULL,

    id_fornecedor INT NULL,

    id_cliente INT NULL,

    id_forma_pagamento INT NOT NULL,

    tipo_movimentacao ENUM('Receita','Despesa') NOT NULL,

    origem VARCHAR(50) NOT NULL,

    id_origem INT NOT NULL,

    data_movimentacao DATE NOT NULL,

    valor DECIMAL(12,2) NOT NULL,

    juros DECIMAL(12,2) DEFAULT 0,

    desconto DECIMAL(12,2) DEFAULT 0,

    valor_liquido DECIMAL(12,2) NOT NULL,

    dias_atraso INT DEFAULT 0,

    status VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_fato_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categorias_financeiras(id_categoria),

    CONSTRAINT fk_fato_centro
        FOREIGN KEY (id_centro_custo)
        REFERENCES centros_custo(id_centro_custo),

    CONSTRAINT fk_fato_banco
        FOREIGN KEY (id_banco)
        REFERENCES bancos(id_banco),

    CONSTRAINT fk_fato_fornecedor
        FOREIGN KEY (id_fornecedor)
        REFERENCES fornecedores(id_fornecedor),

    CONSTRAINT fk_fato_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente),

    CONSTRAINT fk_fato_forma
        FOREIGN KEY (id_forma_pagamento)
        REFERENCES formas_pagamento(id_forma_pagamento)

);