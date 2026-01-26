import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

# CONEXIÓN
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='academiasComboni',
            user='secretaria',
            password='Sec2026'
        )
        return connection
    except Error as e:
        st.error(f"Error de conexión: {e}")
        return None

# --- FUNCIONES QUE LLAMAN A LOS STORED PROCEDURES ---

def insertar_estudiante(id_rep, id_aca, nombre, apellido, promedio, fecha, correo, curso):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            args = (id_rep, id_aca, nombre, apellido, promedio, fecha, correo, curso)
            cursor.callproc('sp_crear_estudiante', args)
            conn.commit()
            st.success("Estudiante registrado mediante SP.")
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def actualizar_estudiante(id_est, nombre, apellido, promedio, curso):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            args = (id_est, nombre, apellido, promedio, curso)
            cursor.callproc('sp_actualizar_estudiante', args)
            conn.commit()
            st.success("Estudiante actualizado mediante SP.")
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def eliminar_estudiante(id_est):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.callproc('sp_eliminar_estudiante', (id_est,))
            conn.commit()
            st.warning("Estudiante eliminado mediante SP.")
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def leer_reporte_estudiantes():
    conn = create_connection()
    if conn:
        try:
            # Llamamos a la VISTA (Reporte) en vez de tabla directa
            query = "SELECT * FROM vista_ficha_estudiante ORDER BY id_estudiante DESC"
            df = pd.read_sql(query, conn)
            conn.close()
            return df
        except Error as e:
            st.error(f"Error al leer reporte: {e}")
            return pd.DataFrame()

# --- INTERFAZ STREAMLIT ---

st.title("Sistema de Gestión Académica")
menu = ["Reportes", "Gestión Estudiantes"]
choice = st.sidebar.selectbox("Menú", menu)

if choice == "Reportes":
    st.subheader("Reporte: Ficha de Estudiantes")
    df = leer_reporte_estudiantes()
    st.dataframe(df)

elif choice == "Gestión Estudiantes":
    accion = st.radio("Acción", ["Registrar", "Actualizar", "Eliminar"])

    if accion == "Registrar":
        c1, c2 = st.columns(2)
        with c1:
            nom = st.text_input("Nombre")
            ape = st.text_input("Apellido")
            email = st.text_input("Correo")
            fnac = st.date_input("Fecha Nacimiento")
        with c2:
            ir = st.number_input("ID Rep.", min_value=1)
            ia = st.number_input("ID Acad.", min_value=1)
            prom = st.number_input("Promedio", 0.0, 10.0)
            cur = st.text_input("Curso")

        if st.button("Guardar"):
            insertar_estudiante(ir, ia, nom, ape, prom, fnac, email, cur)

    elif accion == "Actualizar":
        id_e = st.number_input("ID Estudiante", min_value=1)
        nn = st.text_input("Nuevo Nombre")
        na = st.text_input("Nuevo Apellido")
        np = st.number_input("Nuevo Promedio", 0.0, 10.0)
        nc = st.text_input("Nuevo Curso")
        if st.button("Actualizar"):
            actualizar_estudiante(id_e, nn, na, np, nc)

    elif accion == "Eliminar":
        id_del = st.number_input("ID a Eliminar", min_value=1)
        if st.button("Eliminar"):
            eliminar_estudiante(id_del)
