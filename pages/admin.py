import streamlit as st
import pandas as pd
from crud import (leer_docentes, crear_docente, actualizar_docente, eliminar_docente,
                  leer_representantes, crear_representante, actualizar_representante, eliminar_representante,
                  leer_academias, crear_academia, actualizar_academia, eliminar_academia,
                  leer_estudiantes, crear_estudiante, actualizar_estudiante, eliminar_estudiante,
                  leer_entrenadores, crear_entrenador, actualizar_entrenador, eliminar_entrenador)

st.set_page_config(page_title="Administración", layout="wide")

st.title("Administración")

tab2, tab3, tab4, tab5, tab6 = st.tabs(["Docentes", "Representantes", "Academias", "Estudiantes", "Entrenadores"])

with tab2:
    st.header("Docentes")

    with st.expander("Crear nuevo docente"):
        with st.form("crear_docente_form"):
            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido")
            correo = st.text_input("Correo")
            telefono = st.text_input("Teléfono")
            
            submitted = st.form_submit_button("Crear")
            if submitted:
                crear_docente(nombre, apellido, correo, telefono)
                st.rerun()

    df_docentes = leer_docentes()

    for index, row in df_docentes.iterrows():
        st.subheader(f"{row['nombre']} {row['apellido']}")
        st.write(f"Correo: {row['correo']}")
        st.write(f"Teléfono: {row['telefono']}")

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_docente_{row['id_docente']}"):
                eliminar_docente(row["id_docente"])
                st.rerun()
        
        with col2:
            with st.expander("Editar"):
                with st.form(f"editar_docente_form_{row['id_docente']}"):
                    nombre = st.text_input("Nombre", value=row["nombre"], key=f"edit_nombre_docente_{row['id_docente']}")
                    apellido = st.text_input("Apellido", value=row["apellido"], key=f"edit_apellido_docente_{row['id_docente']}")
                    correo = st.text_input("Correo", value=row["correo"], key=f"edit_correo_docente_{row['id_docente']}")
                    telefono = st.text_input("Teléfono", value=row["telefono"], key=f"edit_telefono_docente_{row['id_docente']}")
                    
                    submitted = st.form_submit_button("Actualizar")
                    if submitted:
                        actualizar_docente(row["id_docente"], nombre, apellido, correo, telefono)
                        st.rerun()

        st.divider()

with tab3:
    st.header("Representantes")

    with st.expander("Crear nuevo representante"):
        with st.form("crear_representante_form"):
            nombre = st.text_input("Nombre")
            telefono = st.text_input("Teléfono")
            correo = st.text_input("Correo")
            clausulas = st.text_input("Cláusulas")
            
            submitted = st.form_submit_button("Crear")
            if submitted:
                crear_representante(nombre, telefono, correo, clausulas)
                st.rerun()

    df_representantes = leer_representantes()

    for index, row in df_representantes.iterrows():
        st.subheader(row["nombre"])
        st.write(f"Teléfono: {row['telefono']}")
        st.write(f"Correo: {row['correo']}")
        st.write(f"Cláusulas: {row['clausulas']}")

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_representante_{row['id_representante']}"):
                eliminar_representante(row["id_representante"])
                st.rerun()
        
        with col2:
            with st.expander("Editar"):
                with st.form(f"editar_representante_form_{row['id_representante']}"):
                    nombre = st.text_input("Nombre", value=row["nombre"], key=f"edit_nombre_representante_{row['id_representante']}")
                    telefono = st.text_input("Teléfono", value=row["telefono"], key=f"edit_telefono_representante_{row['id_representante']}")
                    correo = st.text_input("Correo", value=row["correo"], key=f"edit_correo_representante_{row['id_representante']}")
                    clausulas = st.text_input("Cláusulas", value=row["clausulas"], key=f"edit_clausulas_representante_{row['id_representante']}")
                    
                    submitted = st.form_submit_button("Actualizar")
                    if submitted:
                        actualizar_representante(row["id_representante"], nombre, telefono, correo, clausulas)
                        st.rerun()

        st.divider()

with tab4:
    st.header("Academias")

    with st.expander("Crear nueva academia"):
        with st.form("crear_academia_form"):
            categoria = st.text_input("Categoría")
            n_estudiantes = st.number_input("Número de estudiantes", min_value=0, step=1)
            descripcion = st.text_area("Descripción")
            periodo = st.text_input("Periodo")
            tipo = st.selectbox("Tipo", ['Futbol', 'Basquet', 'Voleibol', 'Cheerleader', 'Kickboxing', 'Robotica'])
            
            submitted = st.form_submit_button("Crear")
            if submitted:
                crear_academia(categoria, n_estudiantes, descripcion, periodo, tipo)
                st.rerun()

    df_academias = leer_academias()

    for index, row in df_academias.iterrows():
        st.subheader(row["categoria"])
        st.write(f"Número de estudiantes: {row['n_estudiantes']}")
        st.write(f"Descripción: {row['descripcion']}")
        st.write(f"Periodo: {row['periodo']}")
        st.write(f"Tipo: {row['tipo']}")


        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_academia_{row['id_academia']}"):
                eliminar_academia(row["id_academia"])
                st.rerun()
        
        with col2:
            with st.expander("Editar"):
                with st.form(f"editar_academia_form_{row['id_academia']}"):
                    categoria = st.text_input("Categoría", value=row["categoria"], key=f"edit_categoria_academia_{row['id_academia']}")
                    n_estudiantes = st.number_input("Número de estudiantes", value=row["n_estudiantes"], min_value=0, step=1, key=f"edit_n_estudiantes_academia_{row['id_academia']}")
                    descripcion = st.text_area("Descripción", value=row["descripcion"], key=f"edit_desc_academia_{row['id_academia']}")
                    periodo = st.text_input("Periodo", value=row["periodo"], key=f"edit_periodo_academia_{row['id_academia']}")
                    
                    tipos = ['Futbol', 'Basquet', 'Voleibol', 'Cheerleader', 'Kickboxing', 'Robotica']
                    current_tipo_index = tipos.index(row["tipo"])
                    tipo = st.selectbox("Tipo", tipos, index=current_tipo_index, key=f"edit_tipo_academia_{row['id_academia']}")
                    
                    submitted = st.form_submit_button("Actualizar")
                    if submitted:
                        actualizar_academia(row["id_academia"], categoria, n_estudiantes, descripcion, periodo, tipo)
                        st.rerun()

        st.divider()

with tab5:
    st.header("Estudiantes")

    with st.expander("Crear nuevo estudiante"):
        with st.form("crear_estudiante_form"):
            nombres = st.text_input("Nombres")
            apellidos = st.text_input("Apellidos")
            promedio = st.number_input("Promedio", min_value=0.0, max_value=10.0, step=0.1)
            fecha_nac = st.date_input("Fecha de nacimiento")
            correo = st.text_input("Correo")
            curso = st.text_input("Curso")

            df_representantes = leer_representantes()
            representante_options = {row["nombre"]: row["id_representante"] for index, row in df_representantes.iterrows()}
            selected_representante_nombre = st.selectbox("Representante", options=list(representante_options.keys()))

            df_academias = leer_academias()
            academia_options = {row["categoria"]: row["id_academia"] for index, row in df_academias.iterrows()}
            selected_academia_nombre = st.selectbox("Academia", options=list(academia_options.keys()))
            
            submitted = st.form_submit_button("Crear")
            if submitted:
                id_representante = representante_options[selected_representante_nombre]
                id_academia = academia_options[selected_academia_nombre]
                crear_estudiante(id_representante, id_academia, nombres, apellidos, promedio, fecha_nac, correo, curso)
                st.rerun()

    df_estudiantes = leer_estudiantes()

    for index, row in df_estudiantes.iterrows():
        st.subheader(f"{row['nombres']} {row['apellidos']}")
        st.write(f"Promedio: {row['promedio']}")
        st.write(f"Fecha de nacimiento: {row['fecha_nac']}")
        st.write(f"Correo: {row['correo']}")
        st.write(f"Curso: {row['curso']}")

        df_representante = leer_representantes()
        representante_nombre = df_representante[df_representante["id_representante"] == row["id_representante"]]["nombre"].iloc[0]
        st.write(f"Representante: {representante_nombre}")

        df_academia = leer_academias()
        academia_nombre = df_academia[df_academia["id_academia"] == row["id_academia"]]["categoria"].iloc[0]
        st.write(f"Academia: {academia_nombre}")

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_estudiante_{row['id_estudiante']}"):
                eliminar_estudiante(row["id_estudiante"])
                st.rerun()

        with col2:
            with st.expander("Editar"):
                with st.form(f"editar_estudiante_form_{row['id_estudiante']}"):
                    nombres = st.text_input("Nombres", value=row["nombres"], key=f"edit_nombres_estudiante_{row['id_estudiante']}")
                    apellidos = st.text_input("Apellidos", value=row["apellidos"], key=f"edit_apellidos_estudiante_{row['id_estudiante']}")
                    promedio = st.number_input("Promedio", value=row["promedio"], min_value=0.0, max_value=10.0, step=0.1, key=f"edit_promedio_estudiante_{row['id_estudiante']}")
                    fecha_nac = st.date_input("Fecha de nacimiento", value=pd.to_datetime(row["fecha_nac"]), key=f"edit_fecha_nac_estudiante_{row['id_estudiante']}")
                    correo = st.text_input("Correo", value=row["correo"], key=f"edit_correo_estudiante_{row['id_estudiante']}")
                    curso = st.text_input("Curso", value=row["curso"], key=f"edit_curso_estudiante_{row['id_estudiante']}")

                    df_representantes = leer_representantes()
                    representante_options = {row_rep["nombre"]: row_rep["id_representante"] for index_rep, row_rep in df_representantes.iterrows()}
                    current_representante_nombre = df_representante[df_representante["id_representante"] == row["id_representante"]]["nombre"].iloc[0]
                    representante_list = list(representante_options.keys())
                    current_representante_index = representante_list.index(current_representante_nombre)
                    selected_representante_nombre = st.selectbox("Representante", options=representante_list, index=current_representante_index, key=f"edit_representante_estudiante_{row['id_estudiante']}")

                    df_academias = leer_academias()
                    academia_options = {row_aca["categoria"]: row_aca["id_academia"] for index_aca, row_aca in df_academias.iterrows()}
                    current_academia_nombre = df_academia[df_academia["id_academia"] == row["id_academia"]]["categoria"].iloc[0]
                    academia_list = list(academia_options.keys())
                    current_academia_index = academia_list.index(current_academia_nombre)
                    selected_academia_nombre = st.selectbox("Academia", options=academia_list, index=current_academia_index, key=f"edit_academia_estudiante_{row['id_estudiante']}")

                    submitted = st.form_submit_button("Actualizar")
                    if submitted:
                        id_representante = representante_options[selected_representante_nombre]
                        id_academia = academia_options[selected_academia_nombre]
                        actualizar_estudiante(row["id_estudiante"], id_representante, id_academia, nombres, apellidos, promedio, fecha_nac, correo, curso)
                        st.rerun()

        st.divider()

with tab6:
    st.header("Entrenadores")

    with st.expander("Crear nuevo entrenador"):
        with st.form("crear_entrenador_form"):
            df_docentes = leer_docentes()
            docente_options = {f"{row['nombre']} {row['apellido']}": row["id_docente"] for index, row in df_docentes.iterrows()}
            selected_docente_nombre = st.selectbox("Docente", options=list(docente_options.keys()))

            academia = st.text_input("Academia")
            
            submitted = st.form_submit_button("Crear")
            if submitted:
                id_docente = docente_options[selected_docente_nombre]
                crear_entrenador(id_docente, academia)
                st.rerun()

    df_entrenadores = leer_entrenadores()

    for index, row in df_entrenadores.iterrows():
        df_docente = leer_docentes()
        docente_info = df_docente[df_docente["id_docente"] == row["id_docente"]].iloc[0]
        st.subheader(f"Entrenador: {docente_info['nombre']} {docente_info['apellido']}")

        st.write(f"Academia: {row['academia']}")

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_entrenador_{row['id_entrenador']}"):
                eliminar_entrenador(row["id_entrenador"])
                st.rerun()

        with col2:
            with st.expander("Editar"):
                with st.form(f"editar_entrenador_form_{row['id_entrenador']}"):
                    df_docentes = leer_docentes()
                    docente_options = {f"{row_doc['nombre']} {row_doc['apellido']}": row_doc["id_docente"] for index_doc, row_doc in df_docentes.iterrows()}
                    current_docente_nombre = f"{docente_info['nombre']} {docente_info['apellido']}"
                    docente_list = list(docente_options.keys())
                    current_docente_index = docente_list.index(current_docente_nombre)
                    selected_docente_nombre = st.selectbox("Docente", options=docente_list, index=current_docente_index, key=f"edit_docente_entrenador_{row['id_entrenador']}")

                    academia = st.text_input("Academia", value=row["academia"], key=f"edit_academia_entrenador_{row['id_entrenador']}")

                    submitted = st.form_submit_button("Actualizar")
                    if submitted:
                        id_docente = docente_options[selected_docente_nombre]
                        actualizar_entrenador(row["id_entrenador"], id_docente, academia)
                        st.rerun()

        st.divider()

