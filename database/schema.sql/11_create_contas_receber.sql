USE financeflow_analytics;

CREATE TABLE contas_receber (

    id_receber INT AUTO_INCREMENT PRIMARY KEY,

    numero_nf VARCHAR(30) NOT NULL,

    id_cliente INT NOT NULL,

    id_categoria INT NOT NULL,

    id_banco INT NOT NULL,

    data_emissao DATE NOT NULL,

    data_vencimento DATE NOT NULL,

    valor DECIMAL(12,2) NOT NULL,

    status ENUM(
        'Pendente',
        'Recebida',
        'Vencida',
        'Cancelada'
    ) DEFAULT 'Pendente',

    observacoes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_cr_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_cr_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categorias_financeiras(id_categoria)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_cr_banco
        FOREIGN KEY (id_banco)
        REFERENCES bancos(id_banco)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_cr_valor
        CHECK (valor > 0),

    CONSTRAINT chk_cr_datas
        CHECK (data_vencimento >= data_emissao)

);
