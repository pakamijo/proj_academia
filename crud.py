import pandas as pd
import streamlit as st
import mysql.connector

def obtener_conexion_db():
    return mysql.connector.connect(
        host='localhost',
        user='admin_sistema',
        password='Admin123',
        database='academiasComboni',
        autocommit=True
    )


def leer_docentes():
    conexion = obtener_conexion_db()
    query = "SELECT * FROM docente"
    
    try:
        df = pd.read_sql(query, conexion)
        return df
    except Exception as e:
        st.error(f"Error en la consulta: {e}")
        return pd.DataFrame
    finally:
        conexion.close()

def crear_docente(nombre, apellido, correo, telefono):
    conexion = obtener_conexion_db()
    query = "INSERT INTO docente (nombre, apellido, correo, telefono) VALUES (%s, %s, %s, %s)"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (nombre, apellido, correo, telefono))
        st.success("Docente creado exitosamente")
    except Exception as e:
        st.error(f"Error al crear el docente: {e}")
    finally:
        conexion.close()

def actualizar_docente(id_docente, nombre, apellido, correo, telefono):
    conexion = obtener_conexion_db()
    query = "UPDATE docente SET nombre = %s, apellido = %s, correo = %s, telefono = %s WHERE id_docente = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (nombre, apellido, correo, telefono, id_docente))
        st.success("Docente actualizado exitosamente")
    except Exception as e:
        st.error(f"Error al actualizar el docente: {e}")
    finally:
        conexion.close()

def eliminar_docente(id_docente):
    conexion = obtener_conexion_db()
    query = "DELETE FROM docente WHERE id_docente = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (id_docente,))
        st.success("Docente eliminado exitosamente")
    except Exception as e:
        st.error(f"Error al eliminar el docente: {e}")
    finally:
        conexion.close()

def obtener_docente(id_docente):
    conexion = obtener_conexion_db()
    query = f"SELECT * FROM docente WHERE id_docente = {id_docente}"
    
    try:
        df = pd.read_sql(query, conexion)
        return df
    except Exception as e:
        st.error(f"Error en la consulta: {e}")
        return pd.DataFrame
    finally:
        conexion.close()


def leer_representantes():
    conexion = obtener_conexion_db()
    query = "SELECT * FROM representante"
    
    try:
        df = pd.read_sql(query, conexion)
        return df
    except Exception as e:
        st.error(f"Error en la consulta: {e}")
        return pd.DataFrame
    finally:
        conexion.close()

def crear_representante(nombre, telefono, correo, clausulas):
    conexion = obtener_conexion_db()
    query = "INSERT INTO representante (nombre, telefono, correo, clausulas) VALUES (%s, %s, %s, %s)"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (nombre, telefono, correo, clausulas))
        st.success("Representante creado exitosamente")
    except Exception as e:
        st.error(f"Error al crear el representante: {e}")
    finally:
        conexion.close()

def actualizar_representante(id_representante, nombre, telefono, correo, clausulas):
    conexion = obtener_conexion_db()
    query = "UPDATE representante SET nombre = %s, telefono = %s, correo = %s, clausulas = %s WHERE id_representante = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (nombre, telefono, correo, clausulas, id_representante))
        st.success("Representante actualizado exitosamente")
    except Exception as e:
        st.error(f"Error al actualizar el representante: {e}")
    finally:
        conexion.close()

def eliminar_representante(id_representante):
    conexion = obtener_conexion_db()
    query = "DELETE FROM representante WHERE id_representante = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (id_representante,))
        st.success("Representante eliminado exitosamente")
    except Exception as e:
        st.error(f"Error al eliminar el representante: {e}")
    finally:
        conexion.close()


def leer_academias():
    conexion = obtener_conexion_db()
    query = "SELECT * FROM academia"
    
    try:
        df = pd.read_sql(query, conexion)
        return df
    except Exception as e:
        st.error(f"Error en la consulta: {e}")
        return pd.DataFrame
    finally:
        conexion.close()

def crear_academia(categoria, n_estudiantes, descripcion, periodo, tipo):
    conexion = obtener_conexion_db()
    query = "INSERT INTO academia (categoria, n_estudiantes, descripcion, periodo, tipo) VALUES (%s, %s, %s, %s, %s)"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (categoria, n_estudiantes, descripcion, periodo, tipo))
        st.success("Academia creada exitosamente")
    except Exception as e:
        st.error(f"Error al crear la academia: {e}")
    finally:
        conexion.close()

def actualizar_academia(id_academia, categoria, n_estudiantes, descripcion, periodo, tipo):
    conexion = obtener_conexion_db()
    query = "UPDATE academia SET categoria = %s, n_estudiantes = %s, descripcion = %s, periodo = %s, tipo = %s WHERE id_academia = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (categoria, n_estudiantes, descripcion, periodo, tipo, id_academia))
        st.success("Academia actualizada exitosamente")
    except Exception as e:
        st.error(f"Error al actualizar la academia: {e}")
    finally:
        conexion.close()

def eliminar_academia(id_academia):
    conexion = obtener_conexion_db()
    query = "DELETE FROM academia WHERE id_academia = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (id_academia,))
        st.success("Academia eliminada exitosamente")
    except Exception as e:
        st.error(f"Error al eliminar la academia: {e}")
    finally:
        conexion.close()


def leer_estudiantes():
    conexion = obtener_conexion_db()
    query = "SELECT * FROM estudiante"
    
    try:
        df = pd.read_sql(query, conexion)
        return df
    except Exception as e:
        st.error(f"Error en la consulta: {e}")
        return pd.DataFrame
    finally:
        conexion.close()

def crear_estudiante(id_representante, id_academia, nombres, apellidos, promedio, fecha_nac, correo, curso):
    conexion = obtener_conexion_db()
    query = "INSERT INTO estudiante (id_representante, id_academia, nombres, apellidos, promedio, fecha_nac, correo, curso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (id_representante, id_academia, nombres, apellidos, promedio, fecha_nac, correo, curso))
        st.success("Estudiante creado exitosamente")
    except Exception as e:
        st.error(f"Error al crear el estudiante: {e}")
    finally:
        conexion.close()

def actualizar_estudiante(id_estudiante, id_representante, id_academia, nombres, apellidos, promedio, fecha_nac, correo, curso):
    conexion = obtener_conexion_db()
    query = "UPDATE estudiante SET id_representante = %s, id_academia = %s, nombres = %s, apellidos = %s, promedio = %s, fecha_nac = %s, correo = %s, curso = %s WHERE id_estudiante = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (id_representante, id_academia, nombres, apellidos, promedio, fecha_nac, correo, curso, id_estudiante))
        st.success("Estudiante actualizado exitosamente")
    except Exception as e:
        st.error(f"Error al actualizar el estudiante: {e}")
    finally:
        conexion.close()

def eliminar_estudiante(id_estudiante):
    conexion = obtener_conexion_db()
    query = "DELETE FROM estudiante WHERE id_estudiante = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (id_estudiante,))
        st.success("Estudiante eliminado exitosamente")
    except Exception as e:
        st.error(f"Error al eliminar el estudiante: {e}")
    finally:
        conexion.close()


def leer_entrenadores():
    conexion = obtener_conexion_db()
    query = "SELECT * FROM entrenador"
    
    try:
        df = pd.read_sql(query, conexion)
        return df
    except Exception as e:
        st.error(f"Error en la consulta: {e}")
        return pd.DataFrame
    finally:
        conexion.close()

def crear_entrenador(id_docente, academia):
    conexion = obtener_conexion_db()
    query = "INSERT INTO entrenador (id_docente, academia) VALUES (%s, %s)"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (id_docente, academia))
        st.success("Entrenador creado exitosamente")
    except Exception as e:
        st.error(f"Error al crear el entrenador: {e}")
    finally:
        conexion.close()

def actualizar_entrenador(id_entrenador, id_docente, academia):
    conexion = obtener_conexion_db()
    query = "UPDATE entrenador SET id_docente = %s, academia = %s WHERE id_entrenador = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (id_docente, academia, id_entrenador))
        st.success("Entrenador actualizado exitosamente")
    except Exception as e:
        st.error(f"Error al actualizar el entrenador: {e}")
    finally:
        conexion.close()

def eliminar_entrenador(id_entrenador):
    conexion = obtener_conexion_db()
    query = "DELETE FROM entrenador WHERE id_entrenador = %s"
    
    try:
        cursor = conexion.cursor()
        cursor.execute(query, (id_entrenador,))
        st.success("Entrenador eliminado exitosamente")
    except Exception as e:
        st.error(f"Error al eliminar el entrenador: {e}")
    finally:
        conexion.close()

