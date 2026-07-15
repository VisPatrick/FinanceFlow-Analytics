USE financeflow_analytics;

CREATE TABLE formas_pagamento (

    id_forma_pagamento INT AUTO_INCREMENT PRIMARY KEY,

    descricao VARCHAR(80) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP

);