USE financeflow_analytics;

CREATE TABLE clientes (

    id_cliente INT AUTO_INCREMENT PRIMARY KEY,

    razao_social VARCHAR(150) NOT NULL,

    nome_fantasia VARCHAR(120),

    cpf_cnpj VARCHAR(18) NOT NULL UNIQUE,

    email VARCHAR(120),

    telefone VARCHAR(20),

    cidade VARCHAR(80),

    estado CHAR(2),

    status ENUM('Ativo','Inativo') DEFAULT 'Ativo',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP

);