USE financeflow_analytics;

CREATE TABLE pagamentos (

    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,

    id_conta INT NOT NULL,

    id_forma_pagamento INT NOT NULL,

    id_banco INT NOT NULL,

    data_pagamento DATE NOT NULL,

    valor_pago DECIMAL(12,2) NOT NULL,

    juros DECIMAL(12,2) DEFAULT 0,

    desconto DECIMAL(12,2) DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_pag_conta
        FOREIGN KEY (id_conta)
        REFERENCES contas_pagar(id_conta)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_pag_forma
        FOREIGN KEY (id_forma_pagamento)
        REFERENCES formas_pagamento(id_forma_pagamento)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_pag_banco
        FOREIGN KEY (id_banco)
        REFERENCES bancos(id_banco)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_pag_valor
        CHECK (valor_pago > 0),

    CONSTRAINT chk_pag_juros
        CHECK (juros >= 0),

    CONSTRAINT chk_pag_desconto
        CHECK (desconto >= 0)

);