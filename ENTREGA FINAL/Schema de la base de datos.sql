USE academiasComboni;

-- ===
-- 1. CREACIÓN DE ÍNDICES
-- ===
CREATE INDEX idx_estudiante_apellido ON estudiante(apellido);
CREATE INDEX idx_representante_telefono ON representante(telefono);
CREATE INDEX idx_pago_fecha ON pago(fecha_pago);
CREATE INDEX idx_competencia_fecha ON competencia(fecha);
CREATE INDEX idx_docente_apellido ON docente(apellido);

-- ===
-- 2. REPORTES (VISTAS)
-- ===

-- Reporte 1: Ficha del Estudiante
CREATE OR REPLACE VIEW vista_ficha_estudiante AS
SELECT 
    E.id_estudiante, E.nombre, E.apellido, 
    A.categoria AS Academia, 
    R.nombre AS Representante, R.telefono
FROM estudiante E
JOIN academia A ON E.id_academia = A.id_academia
JOIN representante R ON E.id_representante = R.id_representante;

-- Reporte 2: Historial de Pagos
CREATE OR REPLACE VIEW vista_historial_pagos AS
SELECT 
    P.fecha_pago, R.nombre AS Pagador, 
    A.categoria AS Academia, P.monto, P.periodo
FROM pago P
JOIN representante R ON P.id_representante = R.id_representante
JOIN academia A ON P.id_academia = A.id_academia;

-- Reporte 3: Resultados de Competencias
CREATE OR REPLACE VIEW vista_competencias_disciplina AS
SELECT 
    C.nombre_competencia, C.fecha, 
    A.categoria, D.nombre AS Disciplina, C.resultado
FROM competencia C
JOIN academia A ON C.id_academia = A.id_academia
JOIN disciplina D ON A.id_disciplina = D.id_disciplina;

-- Reporte 4: Staff de Entrenadores
CREATE OR REPLACE VIEW vista_asignacion_entrenadores AS
SELECT 
    D.nombre, D.apellido, A.categoria AS Academia, D.correo
FROM entrenador En
JOIN docente D ON En.id_docente = D.id_docente
JOIN academia A ON En.id_academia = A.id_academia;

-- ===
-- 3. TRIGGERS
-- ===
DELIMITER //

CREATE TRIGGER trg_incrementar_cupos
AFTER INSERT ON estudiante FOR EACH ROW
BEGIN
    UPDATE academia SET n_estudiantes = n_estudiantes + 1 WHERE id_academia = NEW.id_academia;
END //

CREATE TRIGGER trg_decrementar_cupos
AFTER DELETE ON estudiante FOR EACH ROW
BEGIN
    UPDATE academia SET n_estudiantes = n_estudiantes - 1 WHERE id_academia = OLD.id_academia;
END //

DELIMITER ;

-- ===
-- 4. PROCEDIMIENTOS ALMACENADOS (SPs) CON TRANSACCIONES
-- ===
DELIMITER //

-- Insertar Estudiante
CREATE PROCEDURE sp_crear_estudiante(
    IN p_id_rep INT, IN p_id_aca INT, IN p_nom VARCHAR(100), IN p_ape VARCHAR(50), 
    IN p_prom FLOAT, IN p_nac DATE, IN p_mail VARCHAR(100), IN p_cur VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar estudiante';
    END;
    START TRANSACTION;
        IF p_prom < 0 OR p_prom > 10 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Promedio inválido';
        END IF;
        INSERT INTO estudiante (id_representante, id_academia, nombre, apellido, promedio, fecha_nac, correo, curso)
        VALUES (p_id_rep, p_id_aca, p_nom, p_ape, p_prom, p_nac, p_mail, p_cur);
    COMMIT;
END //

-- Actualizar Estudiante
CREATE PROCEDURE sp_actualizar_estudiante(
    IN p_id INT, IN p_nom VARCHAR(100), IN p_ape VARCHAR(50), 
    IN p_prom FLOAT, IN p_cur VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al actualizar';
    END;
    START TRANSACTION;
        UPDATE estudiante SET nombre = p_nom, apellido = p_ape, promedio = p_prom, curso = p_cur 
        WHERE id_estudiante = p_id;
    COMMIT;
END //

-- Eliminar Estudiante
CREATE PROCEDURE sp_eliminar_estudiante(IN p_id INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al eliminar';
    END;
    START TRANSACTION;
        DELETE FROM estudiante WHERE id_estudiante = p_id;
    COMMIT;
END //
DELIMITER ;

-- ===
-- 5. USUARIOS
-- ===
CREATE USER IF NOT EXISTS 'admin_sistema'@'localhost' IDENTIFIED BY 'Admin123';
GRANT ALL PRIVILEGES ON academiasComboni.* TO 'admin_sistema'@'localhost';

CREATE USER IF NOT EXISTS 'secretaria'@'localhost' IDENTIFIED BY 'Sec2026';
GRANT SELECT ON academiasComboni.* TO 'secretaria'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_crear_estudiante TO 'secretaria'@'localhost';
GRANT EXECUTE ON PROCEDURE sp_actualizar_estudiante TO 'secretaria'@'localhost';

CREATE USER IF NOT EXISTS 'rector'@'localhost' IDENTIFIED BY 'Rector2026';
GRANT SELECT ON academiasComboni.vista_ficha_estudiante TO 'rector'@'localhost';
GRANT SELECT ON academiasComboni.vista_historial_pagos TO 'rector'@'localhost';
GRANT SELECT ON academiasComboni.vista_competencias_disciplina TO 'rector'@'localhost';

CREATE USER IF NOT EXISTS 'cajero'@'localhost' IDENTIFIED BY 'Caja2026';
GRANT SELECT, INSERT ON academiasComboni.pago TO 'cajero'@'localhost';

CREATE USER IF NOT EXISTS 'auditor'@'localhost' IDENTIFIED BY 'Audit2026';
GRANT SELECT ON academiasComboni.estudiante TO 'auditor'@'localhost';
GRANT SELECT ON academiasComboni.pago TO 'auditor'@'localhost';

FLUSH PRIVILEGES;
