USE financeflow_analytics;

CREATE TABLE recebimentos (

    id_recebimento INT AUTO_INCREMENT PRIMARY KEY,

    id_receber INT NOT NULL,

    id_forma_pagamento INT NOT NULL,

    id_banco INT NOT NULL,

    data_recebimento DATE NOT NULL,

    valor_recebido DECIMAL(12,2) NOT NULL,

    juros DECIMAL(12,2) DEFAULT 0,

    desconto DECIMAL(12,2) DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_rec_conta
        FOREIGN KEY (id_receber)
        REFERENCES contas_receber(id_receber)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_rec_forma
        FOREIGN KEY (id_forma_pagamento)
        REFERENCES formas_pagamento(id_forma_pagamento)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_rec_banco
        FOREIGN KEY (id_banco)
        REFERENCES bancos(id_banco)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_rec_valor
        CHECK (valor_recebido > 0)

);