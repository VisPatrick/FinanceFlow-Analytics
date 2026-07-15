USE financeflow_analytics;

CREATE TABLE categorias_financeiras (

    id_categoria INT AUTO_INCREMENT PRIMARY KEY,

    nome_categoria VARCHAR(100) NOT NULL,

    tipo ENUM('Receita','Despesa') NOT NULL,

    descricao TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP

);