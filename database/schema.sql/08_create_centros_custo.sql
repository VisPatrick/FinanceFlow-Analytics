USE financeflow_analytics;

CREATE TABLE centros_custo (

    id_centro_custo INT AUTO_INCREMENT PRIMARY KEY,

    id_departamento INT NOT NULL,

    nome_centro_custo VARCHAR(120) NOT NULL,

    descricao TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_cc_departamento
        FOREIGN KEY (id_departamento)
        REFERENCES departamentos(id_departamento)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

);