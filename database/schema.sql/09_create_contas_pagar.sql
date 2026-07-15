USE financeflow_analytics;

CREATE TABLE contas_pagar (

    id_conta INT AUTO_INCREMENT PRIMARY KEY,

    numero_nf VARCHAR(30) NOT NULL,

    id_fornecedor INT NOT NULL,

    id_categoria INT NOT NULL,

    id_centro_custo INT NOT NULL,

    id_banco INT NOT NULL,

    data_emissao DATE NOT NULL,

    data_vencimento DATE NOT NULL,

    valor DECIMAL(12,2) NOT NULL,

    status ENUM(
        'Pendente',
        'Paga',
        'Vencida',
        'Cancelada'
    ) DEFAULT 'Pendente',

    observacoes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_cp_fornecedor
        FOREIGN KEY (id_fornecedor)
        REFERENCES fornecedores(id_fornecedor)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_cp_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categorias_financeiras(id_categoria)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_cp_centro_custo
        FOREIGN KEY (id_centro_custo)
        REFERENCES centros_custo(id_centro_custo)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_cp_banco
        FOREIGN KEY (id_banco)
        REFERENCES bancos(id_banco)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_cp_valor
        CHECK (valor > 0),

    CONSTRAINT chk_cp_datas
        CHECK (data_vencimento >= data_emissao)

);