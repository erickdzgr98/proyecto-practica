CREATE TABLE IF NOT EXISTS perritos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    raza VARCHAR(50),
    tamanio VARCHAR(20),
    estado_adopcion VARCHAR(20),
    edad_meses INT
);

INSERT INTO perritos (nombre, raza, tamanio, estado_adopcion, edad_meses) VALUES
('Chester', 'Golden Retriever', 'Grande', 'Adoptado', 24),
('Luna', 'Mestizo', 'Mediano', 'Disponible', 8),
('Canela', 'Chihuahua', 'Chico', 'Adoptado', 36),
('Max', 'Pug', 'Chico', 'Disponible', 12),
('Rocky', 'Pastor Alemán', 'Grande', 'En Proceso', 18),
('Bella', 'Mestizo', 'Mediano', 'Adoptado', 14),
('Coco', 'Beagle', 'Mediano', 'Disponible', 6);
