-- Base de datos: academiasComboni
--
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla disciplina
--

CREATE TABLE disciplina (
  id_disciplina int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(50) NOT NULL,
  descripcion varchar(50) DEFAULT NULL
);

--
-- Volcado de datos para la tabla disciplina
--

INSERT INTO disciplina (id_disciplina, nombre, descripcion) VALUES
(1, 'Futbol', 'Deporte de campo'),
(2, 'Baloncesto', 'Deporte de canasta'),
(3, 'Voleibol', 'Deporte de red'),
(4, 'Cheerleader', 'Animacion y acrobacia'),
(5, 'Kickboxing', 'Contacto y defensa'),
(6, 'Robotica', 'Tecnologia y programacion'),
(7, 'Futbol Sala', 'Variante de futbol'),
(8, 'Voleibol Playa', 'Variante de voleibol'),
(9, 'Baloncesto 3x3', 'Variante de baloncesto'),
(10, 'Robotica Avanzada', 'Programacion compleja');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla representante
--

CREATE TABLE representante (
  id_representante int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(100) NOT NULL,
  telefono varchar(10) DEFAULT NULL,
  correo varchar(100) DEFAULT NULL,
  clausulas varchar(100) DEFAULT NULL
);

--
-- Volcado de datos para la tabla representante
--

INSERT INTO representante (id_representante, nombre, telefono, correo, clausulas) VALUES
(1, 'Carlos Perez', '0991112222', 'carlos@mail.com', 'Ninguna'),
(2, 'Maria Lopez', '0993334444', 'maria@mail.com', 'Pago anticipado'),
(3, 'Juan Diaz', '0995556666', 'juan@mail.com', 'Becado'),
(4, 'Luisa Mendez', '0987778888', 'luisa@mail.com', 'Pago mensual'),
(5, 'Pedro Gomez', '0990001111', 'pedro@mail.com', 'Ninguna'),
(6, 'Ana Ruiz', '0982223333', 'ana@mail.com', 'Descuento hermano'),
(7, 'Jose Vera', '0994445555', 'jose@mail.com', 'Ninguna'),
(8, 'Sofia Castro', '0986667777', 'sofia@mail.com', 'Pago anual'),
(9, 'Miguel Torres', '0998889999', 'miguel@mail.com', 'Ninguna'),
(10, 'Elena Silva', '0981231234', 'elena@mail.com', 'Ninguna');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla docente
--

CREATE TABLE docente (
  id_docente int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(100) NOT NULL,
  apellido varchar(100) NOT NULL,
  correo varchar(100) DEFAULT NULL,
  telefono varchar(10) DEFAULT NULL
);

--
-- Volcado de datos para la tabla docente
--

INSERT INTO docente (id_docente, nombre, apellido, correo, telefono) VALUES
(1, 'Roberto', 'Gomez', 'roberto@comboni.edu', '0987654321'),
(2, 'Laura', 'Martinez', 'laura@comboni.edu', '0981234567'),
(3, 'Fernando', 'Alvarez', 'fer@comboni.edu', '0998765432'),
(4, 'Patricia', 'Suarez', 'paty@comboni.edu', '0991230987'),
(5, 'Diego', 'Ramirez', 'diego@comboni.edu', '0985551111'),
(6, 'Carmen', 'Ortiz', 'carmen@comboni.edu', '0992223344'),
(7, 'Ricardo', 'Lara', 'ricardo@comboni.edu', '0984445566'),
(8, 'Silvia', 'Mora', 'silvia@comboni.edu', '0996667788'),
(9, 'Andres', 'Paredes', 'andres@comboni.edu', '0988889900'),
(10, 'Gabriela', 'Leon', 'gaby@comboni.edu', '0990001122');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla materia
--

CREATE TABLE materia (
  id_materia int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  materia varchar(100) NOT NULL
);

--
-- Volcado de datos para la tabla materia
--

INSERT INTO materia (id_materia, materia) VALUES
(1, 'Técnica Individual'), (2, 'Estrategia de Juego'), (3, 'Acondicionamiento Físico'), 
(4, 'Programación Básica'), (5, 'Coreografía'), (6, 'Defensa Personal'), 
(7, 'Nutrición Deportiva'), (8, 'Reglamento'), (9, 'Psicología Deportiva'), (10, 'Primeros Auxilios');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla academia
--

CREATE TABLE academia (
  id_academia int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  categoria varchar(50) NOT NULL,
  n_estudiantes int DEFAULT 0,
  fecha_creacion date DEFAULT NULL,
  descripcion varchar(255) DEFAULT NULL,
  id_disciplina int NOT NULL,
  periodo varchar(100) DEFAULT NULL,
  FOREIGN KEY (id_disciplina) REFERENCES disciplina (id_disciplina)
);

--
-- Volcado de datos para la tabla academia
--

INSERT INTO academia (id_academia, categoria, n_estudiantes, fecha_creacion, descripcion, id_disciplina, periodo) VALUES
(1, 'Futbol Sub 10', 20, '2020-01-15', 'Iniciacion', 1, '2025-A'),
(2, 'Futbol Sub 15', 18, '2019-05-20', 'Competencia', 1, '2025-A'),
(3, 'Baloncesto Mini', 15, '2021-03-10', 'Formativa', 2, '2025-A'),
(4, 'Baloncesto Juvenil', 12, '2022-02-14', 'Seleccion', 2, '2025-A'),
(5, 'Voleibol Mixto', 10, '2023-06-01', 'Recreativo', 3, '2025-B'),
(6, 'Voleibol Damas', 14, '2021-09-09', 'Competencia', 3, '2025-B'),
(7, 'Cheerleader Kids', 16, '2020-04-20', 'Animacion', 4, '2025-A'),
(8, 'Cheerleader Elite', 12, '2019-11-11', 'Acrobacias', 4, '2025-A'),
(9, 'Kickboxing Defensa', 9, '2022-07-15', 'Defensa', 5, '2025-B'),
(10, 'Robotica LEGO', 6, '2019-12-01', 'Programacion', 6, '2025-A');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla curso
--

CREATE TABLE curso (
  id_curso int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_docente int NOT NULL,
  curso varchar(100) NOT NULL,
  FOREIGN KEY (id_docente) REFERENCES docente (id_docente)
);

--
-- Volcado de datos para la tabla curso
--

INSERT INTO curso (id_curso, id_docente, curso) VALUES
(1, 1, '10mo A'), (2, 2, '8vo B'), (3, 3, '1ro Bach'), (4, 4, '9no A'), (5, 5, '7mo C'),
(6, 6, '10mo B'), (7, 7, '1ro Bach B'), (8, 8, '8vo A'), (9, 9, '9no B'), (10, 10, '7mo A');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla docente_materia
--

CREATE TABLE docente_materia (
  id_docente int NOT NULL,
  id_materia int NOT NULL,
  PRIMARY KEY (id_docente, id_materia),
  FOREIGN KEY (id_docente) REFERENCES docente (id_docente),
  FOREIGN KEY (id_materia) REFERENCES materia (id_materia)
);

--
-- Volcado de datos para la tabla docente_materia
--

INSERT INTO docente_materia (id_docente, id_materia) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (7, 7), (8, 8), (9, 9), (10, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla estudiante
--

CREATE TABLE estudiante (
  id_estudiante int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_representante int NOT NULL,
  id_academia int NOT NULL,
  nombre varchar(100) NOT NULL,
  apellido varchar(50) NOT NULL,
  promedio float DEFAULT NULL,
  fecha_nac date DEFAULT NULL,
  correo varchar(100) DEFAULT NULL,
  curso varchar(100) DEFAULT NULL,
  FOREIGN KEY (id_representante) REFERENCES representante (id_representante),
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

--
-- Volcado de datos para la tabla estudiante
--

INSERT INTO estudiante (id_representante, id_academia, nombre, apellido, promedio, fecha_nac, correo, curso) VALUES
(1, 1, 'Pedrito', 'Perez', 9.5, '2010-05-15', 'pedro@mail.com', '10mo A'),
(2, 2, 'Anita', 'Lopez', 8.0, '2012-08-20', 'ana@mail.com', '8vo B'),
(3, 3, 'Luisito', 'Diaz', 7.5, '2009-12-01', 'luis@mail.com', '1ro Bach'),
(4, 1, 'Marquitos', 'Mendez', 8.8, '2010-02-10', 'marcos@mail.com', '10mo B'),
(5, 5, 'Javier', 'Gomez', 9.0, '2011-06-15', 'javi@mail.com', '9no A'),
(6, 6, 'Lucia', 'Ruiz', 9.2, '2008-11-30', 'lucia@mail.com', '2do Bach'),
(7, 7, 'Mateo', 'Vera', 7.8, '2009-04-25', 'mateo@mail.com', '1ro Bach'),
(8, 8, 'Camila', 'Castro', 8.5, '2012-01-05', 'cami@mail.com', '8vo A'),
(9, 9, 'Daniel', 'Torres', 10.0, '2010-09-12', 'dani@mail.com', '10mo C'),
(10, 10, 'Valeria', 'Silva', 9.1, '2011-03-22', 'vale@mail.com', '9no B');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla entrenador
--

CREATE TABLE entrenador (
  id_entrenador int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_docente int NOT NULL,
  id_academia int NOT NULL,
  FOREIGN KEY (id_docente) REFERENCES docente (id_docente),
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

--
-- Volcado de datos para la tabla entrenador
--

INSERT INTO entrenador (id_docente, id_academia) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla coordinador
--

CREATE TABLE coordinador (
  id_coordinador int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_docente int NOT NULL,
  id_academia int NOT NULL,
  FOREIGN KEY (id_docente) REFERENCES docente (id_docente),
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

--
-- Volcado de datos para la tabla coordinador
--

INSERT INTO coordinador (id_docente, id_academia) VALUES
(10, 1), (9, 2), (8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8), (2, 9), (1, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla entrenamiento
--

CREATE TABLE entrenamiento (
  id_entrenamiento int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_academia int NOT NULL,
  horario varchar(100) DEFAULT NULL,
  horario_2 varchar(100) DEFAULT NULL,
  horario_3 varchar(100) DEFAULT NULL,
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

--
-- Volcado de datos para la tabla entrenamiento
--

INSERT INTO entrenamiento (id_academia, horario, horario_2, horario_3) VALUES
(1, '08:00', '16:00', NULL), (2, '07:00', '15:00', NULL), (3, '09:00', '17:00', NULL),
(4, '10:00', NULL, NULL), (5, '15:00', '18:00', NULL), (6, '06:00', '18:00', NULL),
(7, '05:00', NULL, NULL), (8, '14:00', NULL, NULL), (9, '16:00', '10:00', NULL), (10, '19:00', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla competencia
--

CREATE TABLE competencia (
  id_competencia int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_academia int NOT NULL,
  nombre_competencia varchar(100) DEFAULT NULL,
  fecha date DEFAULT NULL,
  lugar_competencia varchar(100) DEFAULT NULL,
  resultado varchar(100) DEFAULT NULL,
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

--
-- Volcado de datos para la tabla competencia
--

INSERT INTO competencia (id_academia, nombre_competencia, fecha, lugar_competencia, resultado) VALUES
(1, 'Copa Futbol', '2025-12-15', 'Estadio', 'Campeones'), (2, 'Torneo Juvenil', '2025-11-20', 'Cancha Sur', '3er Lugar'),
(3, 'Liga Basket', '2025-10-10', 'Coliseo', 'Subcampeones'), (4, 'Intercolegial', '2025-09-05', 'Cancha N', 'Ganado'),
(5, 'Abierto Voley', '2025-08-15', 'Coliseo', '1er Lugar'), (6, 'Copa Damas', '2025-07-20', 'Coliseo A', 'Cuartos'),
(7, 'Cheerleader', '2025-06-10', 'Teatro', '5to Lugar'), (8, 'Nacional Cheer', '2025-05-05', 'Guayaquil', 'Presentacion'),
(9, 'Torneo Kick', '2025-04-12', 'Gimnasio', '2do Lugar'), (10, 'Feria Robo', '2025-03-30', 'Universidad', 'Mejor Proy');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla pago
--

CREATE TABLE pago (
  id_pago int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_representante int NOT NULL,
  id_academia int NOT NULL,
  fecha_pago date DEFAULT NULL,
  monto float DEFAULT NULL,
  periodo varchar(100) DEFAULT NULL,
  FOREIGN KEY (id_representante) REFERENCES representante (id_representante),
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia)
);

--
-- Volcado de datos para la tabla pago
--

INSERT INTO pago (id_representante, id_academia, fecha_pago, monto, periodo) VALUES
(1, 1, '2026-01-05', 50.00, 'Enero 2026'), (2, 2, '2026-01-05', 45.00, 'Enero 2026'),
(3, 3, '2026-01-06', 60.00, 'Enero 2026'), (4, 1, '2026-01-07', 50.00, 'Enero 2026'),
(5, 5, '2026-01-08', 40.00, 'Enero 2026'), (6, 6, '2026-01-10', 70.00, 'Enero 2026'),
(7, 7, '2026-01-12', 35.00, 'Enero 2026'), (8, 8, '2026-01-15', 55.00, 'Enero 2026'),
(9, 9, '2026-01-20', 45.00, 'Enero 2026'), (10, 10, '2026-01-25', 50.00, 'Enero 2026');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla asistencia
--

CREATE TABLE asistencia (
  id_asistencia int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_academia int NOT NULL,
  id_estudiante int NOT NULL,
  fecha date DEFAULT NULL,
  estado enum('Presente','Ausente','Atraso','Justificado') DEFAULT NULL,
  FOREIGN KEY (id_academia) REFERENCES academia (id_academia),
  FOREIGN KEY (id_estudiante) REFERENCES estudiante (id_estudiante)
);

--
-- Volcado de datos para la tabla asistencia
--

INSERT INTO asistencia (id_academia, id_estudiante, fecha, estado) VALUES
(1, 1, '2026-01-10', 'Presente'), (2, 2, '2026-01-10', 'Presente'), (3, 3, '2026-01-10', 'Ausente'),
(1, 4, '2026-01-10', 'Presente'), (5, 5, '2026-01-10', 'Atraso'), (6, 6, '2026-01-10', 'Presente'),
(7, 7, '2026-01-10', 'Justificado'), (8, 8, '2026-01-10', 'Presente'), (9, 9, '2026-01-10', 'Presente'),
(10, 10, '2026-01-10', 'Ausente');