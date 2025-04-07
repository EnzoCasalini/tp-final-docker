CREATE TABLE IF NOT EXISTS adresse (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_rue VARCHAR(10),
    nom_rue VARCHAR(255),
    ville VARCHAR(100),
    code_postal VARCHAR(10)
);