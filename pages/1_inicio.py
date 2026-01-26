import streamlit as st
import mysql.connector
import base64
import os
import pandas as pd

def obtener_conexion_db():
    return mysql.connector.connect(
        host='localhost',
        user='secretaria',
        password='Sec2026',
        database='academiasComboni',
        autocommit=True
    )

def get_img_as_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""
    
@st.cache_data
def obtener_tipos_academia_db():
    conexion = obtener_conexion_db()
    query = "SELECT DISTINCT tipo FROM academia"
    
    try:
        df = pd.read_sql(query, conexion)
        return df
    except Exception as e:
        st.error(f"Error en la consulta: {e}")
        return pd.DataFrame
    finally:
        conexion.close()
        
df_tipos_academia = obtener_tipos_academia_db()

def obtener_info_docente(tipo_academia):
    conexion = obtener_conexion_db()
    query = f"""
        SELECT d.nombre, d.apellido, d.correo, d.telefono 
        FROM docente d 
        JOIN impartir i ON d.id_docente = i.id_docente
        JOIN academia a ON i.id_academia = a.id_academia
        WHERE a.tipo = '{tipo_academia}'
        LIMIT 1
    """
    try:
        df = pd.read_sql(query, conexion)
        if not df.empty:
            return df.iloc[0]
        return None
    except Exception as e:
        return None 
    finally:
        conexion.close()

def obtener_info_estudiantes(tipo_academia):
    conexion = obtener_conexion_db()
    
    query = f"""
        SELECT e.nombres, e.apellidos, e.correo, e.curso, a.categoria, e.promedio
        FROM estudiante as e
        JOIN academia as a using(id_academia)
        WHERE a.tipo = '{tipo_academia}'
    """
    try:
        df = pd.read_sql(query, conexion)
        return df
    except Exception as e:
        st.error(f"Error cargando estudiantes: {e}")
        return pd.DataFrame()
    finally:
        conexion.close()
    
def mostrar_header():
    col_izq, col_centro, col_der = st.columns([1,10,1])
    
    with col_centro:
        st.markdown("<h1 style='text-align: center;'>ACADEMIAS</h1>", unsafe_allow_html=True)
        
    with col_der:   
        img_path = "usuario.png"
        if os.path.exists(img_path):
            st.image(img_path, width=75)
        else:
            st.warning("Sin imagen")
    st.divider()


def mostrar_central():
    st.markdown('<div style="height: 5vh;"></div>', unsafe_allow_html=True)
    
    img_b64 = get_img_as_base64("uepdcsin.png")
    img_html = f'<img src="data:image/png;base64,{img_b64}" style="max-height: 150px; width: auto;">'
        
    st.markdown(f"""
        <div style="
            min-height: 30vh; 
            display: flex; 
            flex-direction: column; 
            justify-content: center; 
            align-items: center; 
            width: 100%;
        ">
            <h2 style='text-align: center; margin: 0;'>Unidad Educativa</h2>
            <div style="margin: 20px 0;">
                {img_html}
            </div>
            <h2 style='text-align: center; margin: 0;'>Daniel Comboni</h2>
        </div>
    """, unsafe_allow_html=True)
    
    if df_tipos_academia.empty:
        st.info("No hay academias registradas en la base de datos.")
        return
    
    col1, col_academias1, col_academias2, col3 = st.columns([1,2,2,1])

    for index, columna in df_tipos_academia.iterrows():
        tipo_academia = columna['tipo'] 
        
        def seleccionar_academia(nombre=tipo_academia):
            st.session_state['academia_seleccionada'] = nombre
            st.session_state['pagina'] = 'detalle'
        
        if index % 2 == 0:
            with col_academias1:
                st.button(tipo_academia, use_container_width=True, key=f"btn_{index}", on_click=seleccionar_academia)
        else:
            with col_academias2:
                st.button(tipo_academia, use_container_width=True, key=f"btn_{index}", on_click=seleccionar_academia)


def mostrar_footer():
    st.divider()
    st.markdown("""
        <style>
            .footer-container {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #0E1117;
                border-top: 1px solid #333;
                padding: 10px 20px;
                z-index: 999;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer-container">', unsafe_allow_html=True)
    
    col_izq, col_centro, col_der = st.columns([1, 3, 0.3])

    with col_izq:
        st.subheader("Contáctanos:")
        
    with col_centro:
        st.write("**Email:** secretaria@uepdc.edu.ec")
        st.write("**Telf:** +593 98 765 4321")
        
    with col_der:
        img_path = "uepdcsin.png"
        if os.path.exists(img_path):
            st.image(img_path, width=50)
        else:
            st.warning("Sin img")
            
    st.markdown('</div>', unsafe_allow_html=True)
    
    
def mostrar_detalle_academia():
    academia = st.session_state['academia_seleccionada']
    
    if st.button("← Regresar"):
        st.session_state['pagina'] = 'inicio'
        st.rerun()

    col_academia, col_vacia , col_docente = st.columns([1, 2, 1])
   
    with col_academia:
        st.markdown(f'<h1 style="margin-bottom: 0;">{academia.capitalize()}</h1>', unsafe_allow_html=True)
        conexion = obtener_conexion_db()
        try:
            query = f"select count(*) as total from estudiante e join academia a using(id_academia) where a.tipo = '{academia}'"
            df = pd.read_sql(query, conexion)
            total = df.iloc[0]['total']
            st.caption(f"{total} estudiantes")
        except Exception as e:
            st.error("Error cargando datos")
        finally:
            conexion.close()
        
    with col_docente:
        datos_docente = obtener_info_docente(academia)
        
        nombre_doc = "Por asignar"
        correo_doc = "---"
        telf_doc = "---"
        
        if datos_docente is not None:
            nombre_doc = f"{datos_docente['nombre']} {datos_docente['apellido']}"
            correo_doc = datos_docente['correo']
            telf_doc = datos_docente['telefono']

        img_user_b64 = get_img_as_base64("usuario.png")
        
        st.markdown(f"""
            <div style="
                display: flex;
                align-items: center;
                justify-content: flex-start;
                gap: 15px;
            ">
                <div style="text-align: left;">
                    <h4 style="margin:0; font-weight: bold;">DOCENTE</h4> 
                    <p style="margin:5px 0; font-size: 1.1em;">{nombre_doc}</p>
                    <p style="margin:0; font-size: 0.85em;">{correo_doc}</p>
                    <p style="margin:0; font-size: 0.85em;">{telf_doc}</p>
                </div>
                <div>
                    <img src="data:image/png;base64,{img_user_b64}"
                         style="width: 50%; height: 50%; border-radius: 50%; object-fit: cover; /* Se eliminó el borde de la imagen */">
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.write("")

    tab1, tab2, tab3, tab4, tab5= st.tabs(["Estudiantes", "Asistencia", "Horario", "Deudas","✏️"])

    with tab1:
        col_espacio, col_filtros = st.columns([8, 2])
        with col_filtros:
            st.button("Filtros ⚙️", use_container_width=True)

        df_estudiantes = obtener_info_estudiantes(academia)

        if df_estudiantes.empty:
            st.info("No hay estudiantes inscritos en esta academia aún.")
        else:
            df_estudiantes = df_estudiantes.rename(columns={
                "nombres": "Nombres",
                "apellidos": "Apellidos",
                "correo": "Correo",
                "curso": "Curso",
                "categoria": "Categoría",
                "promedio": "Promedio"
            })

            st.dataframe(
                df_estudiantes, 
                use_container_width=True, 
                hide_index=True,
                column_config={
                    "Promedio": st.column_config.NumberColumn(
                        "Promedio",
                        format="%.2f"
                    )
                }
            )

    with tab2:
        st.info("Módulo de Asistencia en construcción")

if 'pagina' not in st.session_state:
    st.session_state['pagina'] = 'inicio'

if st.session_state['pagina'] == 'inicio':
    mostrar_header()
    mostrar_central()
    st.markdown('<div style="height: 20vh;"></div>', unsafe_allow_html=True)
    mostrar_footer()
elif st.session_state['pagina'] == 'detalle':
    mostrar_detalle_academia()
