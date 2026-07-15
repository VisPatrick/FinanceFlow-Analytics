
CREATE TABLE departamentos (
	id_departamento INT auto_increment PRIMARY KEY,
    
    nome_departamento VARCHAR(100) NOT NULL,
    
	gestor VARCHAR(120),
    
    descricao TEXT,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
	update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP
    
);
