DROP DATABASE IF EXISTS academiasComboni;
CREATE DATABASE academiasComboni;
USE academiasComboni;

-- ==========================================================
-- 1. TABLAS INDEPENDIENTES Y PADRES
-- ==========================================================

-- Tabla 1: Representante
CREATE TABLE representante (
  id_representante int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(100) NOT NULL,
  telefono varchar(20) DEFAULT NULL,
  correo varchar(100) DEFAULT NULL,
  clausulas varchar(500) DEFAULT NULL
);

-- Tabla 2: Docente
CREATE TABLE docente (
  id_docente int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(100) NOT NULL,
  apellido varchar(100) NOT NULL,
  correo varchar(100) DEFAULT NULL,
  telefono varchar(20) DEFAULT NULL
);

-- Tabla 3: Academia
CREATE TABLE academia (
  id_academia int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  categoria varchar(50) NOT NULL,
  n_estudiantes int DEFAULT 0,
  periodo varchar(50) DEFAULT NULL,
  descripcion varchar(255) DEFAULT NULL,
  tipo ENUM('Futbol', 'Basquet', 'Voleibol', 'Cheerleader', 'Kickboxing', 'Robotica') NOT NULL
);

-- ==========================================================
-- 2. TABLAS DE RELACIÓN Y DETALLES ACADÉMICOS
-- ==========================================================

-- Tabla 4: Materia 
CREATE TABLE materia (
  id_materia int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre_materia varchar(100) NOT NULL,
  id_docente int NOT NULL,
  FOREIGN KEY (id_docente) REFERENCES docente (id_docente)
);

-- Tabla 5: Curso 
CREATE TABLE curso (
  id_curso int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre_curso varchar(100) NOT NULL,
  id_docente int NOT NULL,
  FOREIGN KEY (id_docente) REFERENCES docente (id_docente)
);

-- Tabla 6: Estudiante
CREATE TABLE estudiante (
  id_estudiante int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_representante int NOT NULL,
  id_academia int NOT NULL,
  nombres varchar(100) NOT NULL,
  apellidos varchar(100) NOT NULL,
  fecha_nac date DEFAULT NULL,
  promedio float DEFAULT NULL,
  correo varchar(100) DEFAULT NULL,
  curso varchar(50) DEFAULT NULL,
  FOREIGN KEY (id_representante) REFERENCES representante (id_representante),
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

-- Tabla 7: Deuda 
CREATE TABLE deuda (
  id_deuda int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_estudiante int NOT NULL,
  tipo varchar(100) DEFAULT NULL,
  mes varchar(20) DEFAULT NULL,
  FOREIGN KEY (id_estudiante) REFERENCES estudiante (id_estudiante)
);

-- Tabla 8: Pago 
CREATE TABLE pago (
  id_pago int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_representante int NOT NULL,
  id_academia int NOT NULL,
  id_deuda int DEFAULT NULL,
  fecha_pago date DEFAULT NULL,
  monto int DEFAULT NULL,
  FOREIGN KEY (id_representante) REFERENCES representante (id_representante),
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia),
  FOREIGN KEY (id_deuda) REFERENCES deuda (id_deuda)
);

-- Tabla 9: Impartir 
CREATE TABLE impartir (
  id_docente int NOT NULL,
  id_academia int NOT NULL,
  PRIMARY KEY (id_docente, id_academia),
  FOREIGN KEY (id_docente) REFERENCES docente (id_docente),
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

-- ==========================================================
-- 3. SUBTIPOS DE DOCENTE Y ACTIVIDADES
-- ==========================================================

-- Tabla 10: Entrenador 
-- En el PDF tiene atributo 'academia' (varchar), no FK.
CREATE TABLE entrenador (
  id_entrenador int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_docente int NOT NULL,
  academia varchar(50) DEFAULT NULL, 
  FOREIGN KEY (id_docente) REFERENCES docente (id_docente)
);

-- Tabla 11: Coordinador 
-- En el PDF tiene 'tipo' enum.
CREATE TABLE coordinador (
  id_coordinador int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_docente int NOT NULL,
  tipo ENUM('Deportes', 'Robotica') DEFAULT NULL,
  FOREIGN KEY (id_docente) REFERENCES docente (id_docente)
);

-- Tabla 12: Entrenamiento
CREATE TABLE entrenamiento (
  id_entrenamiento int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_academia int NOT NULL,
  horario varchar(100) DEFAULT NULL,
  dia varchar(100) DEFAULT NULL,
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

-- Tabla 13: Competencia
CREATE TABLE competencia (
  id_competencia int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_academia int NOT NULL,
  fecha date DEFAULT NULL,
  nombre varchar(100) DEFAULT NULL,
  lugar varchar(255) DEFAULT NULL,
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

-- ==========================================================
-- 4. INSERCIÓN DE VOLCADO DE DATOS 
-- ==========================================================

INSERT INTO representante (nombre, telefono, correo, clausulas) VALUES
('Carlos Perez', '099111255', 'carlos@Gmail.com', 'Ninguna'),
('Maria Lopez', '0993334423', 'maria@Gmail.com', 'Pago anticipado'),
('Juan Diaz', '0995556611', 'juan@Gmail.com', 'Becado'),
('Luisa Mendez', '0987778802', 'luisa@Gmail.com', 'Pago mensual'),
('Pedro Gomez', '0990001256', 'pedro@Gmail.com', 'Ninguna');

INSERT INTO docente (nombre, apellido, correo, telefono) VALUES
('Roberto', 'Gomez', 'roberto@comboni.edu', '0987654321'),
('Laura', 'Martinez', 'laura@comboni.edu', '0981234567'),
('Fernando', 'Alvarez', 'fer@comboni.edu', '0998765432'),
('Patricia', 'Suarez', 'paty@comboni.edu', '0991230987'),
('Diego', 'Ramirez', 'diego@comboni.edu', '0985551111');

-- Datos ENUM de Tipo
INSERT INTO academia (categoria, n_estudiantes, periodo, descripcion, tipo) VALUES
('Futbol Sub 10', 20, '2025-A', 'Iniciacion', 'Futbol'),
('Baloncesto Mini', 15, '2025-A', 'Formativa', 'Basquet'),
('Voleibol Mixto', 10, '2025-B', 'Recreativo', 'Voleibol'),
('Cheerleader Kids', 16, '2025-A', 'Animacion', 'Cheerleader'),
('Robotica LEGO', 6, '2025-A', 'Programacion', 'Robotica');

-- Relación IMPARTIR 
INSERT INTO impartir (id_docente, id_academia) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5);

INSERT INTO materia (nombre_materia, id_docente) VALUES
('Técnica Individual', 1), ('Estrategia', 2), ('Físico', 3), ('Coreografía', 4), ('Programación', 5);

INSERT INTO curso (nombre_curso, id_docente) VALUES
('10mo A', 1), ('8vo B', 2), ('1ro Bach', 3), ('9no A', 4), ('7mo C', 5);

INSERT INTO estudiante (id_representante, id_academia, nombres, apellidos, promedio, fecha_nac, correo, curso) VALUES
(1, 1, 'Pedrito', 'Perez', 9.5, '2010-05-15', 'pedro@mail.com', '10mo A'),
(2, 2, 'Anita', 'Lopez', 8.0, '2012-08-20', 'ana@mail.com', '8vo B'),
(3, 3, 'Luisito', 'Diaz', 7.5, '2009-12-01', 'luis@mail.com', '1ro Bach'),
(4, 4, 'Marquitos', 'Mendez', 8.8, '2010-02-10', 'marcos@mail.com', '9no A'),
(5, 5, 'Javier', 'Gomez', 9.0, '2011-06-15', 'javi@mail.com', '7mo C');

-- Deudas 
INSERT INTO deuda (id_estudiante, tipo, mes) VALUES
(1, 'Mensualidad', 'Enero'), (2, 'Matricula', 'Enero'), (3, 'Mensualidad', 'Febrero'), 
(4, 'Uniforme', 'Marzo'), (5, 'Mensualidad', 'Enero');

-- Pagos 
INSERT INTO pago (id_representante, id_academia, id_deuda, fecha_pago, monto) VALUES
(1, 1, 1, '2026-01-05', 50), (2, 2, 2, '2026-01-06', 45), (3, 3, 3, '2026-02-01', 60), 
(4, 4, 4, '2026-03-10', 50), (5, 5, 5, '2026-01-15', 40);

INSERT INTO entrenador (id_docente, academia) VALUES
(1, 'Academia Central'), (2, 'Norte'), (3, 'Sur');

INSERT INTO coordinador (id_docente, tipo) VALUES
(4, 'Deportes'), (5, 'Robotica');

INSERT INTO entrenamiento (id_academia, horario, dia) VALUES
(1, '08:00 - 10:00', 'Lunes'), (2, '15:00 - 17:00', 'Martes'), (3, '16:00 - 18:00', 'Miercoles');

INSERT INTO competencia (id_academia, fecha, nombre, lugar) VALUES
(1, '2025-12-15', 'Copa Navidad', 'Estadio Central'), (2, '2025-11-20', 'Intercolegial', 'Coliseo Mayor');