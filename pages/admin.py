import streamlit as st
import pandas as pd
from crud import (read_disciplinas, create_disciplina, update_disciplina, delete_disciplina, 
                  read_docentes, create_docente, update_docente, delete_docente,
                  read_representantes, create_representante, update_representante, delete_representante,
                  read_academias, create_academia, update_academia, delete_academia,
                  read_estudiantes, create_estudiante, update_estudiante, delete_estudiante,
                  read_entrenadores, create_entrenador, update_entrenador, delete_entrenador)

st.set_page_config(page_title="Administración", layout="wide")

st.title("Administración")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Disciplinas", "Docentes", "Representantes", "Academias", "Estudiantes", "Entrenadores"])

with tab1:
    st.header("Disciplinas")

    with st.expander("Crear nueva disciplina"):
        with st.form("crear_disciplina_form"):
            nombre = st.text_input("Nombre")
            descripcion = st.text_area("Descripción")
            
            submitted = st.form_submit_button("Crear")
            if submitted:
                create_disciplina(nombre, descripcion)
                st.rerun()

    df_disciplinas = read_disciplinas()

    for index, row in df_disciplinas.iterrows():
        st.subheader(row["nombre"])
        st.write(row["descripcion"])

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_disciplina_{row['id_disciplina']}"):
                delete_disciplina(row["id_disciplina"])
                st.rerun()
        
        with col2:
            with st.expander("Editar"):
                with st.form(f"editar_disciplina_form_{row['id_disciplina']}"):
                    nombre = st.text_input("Nombre", value=row["nombre"], key=f"edit_nombre_disciplina_{row['id_disciplina']}")
                    descripcion = st.text_area("Descripción", value=row["descripcion"], key=f"edit_desc_disciplina_{row['id_disciplina']}")
                    
                    submitted = st.form_submit_button("Actualizar")
                    if submitted:
                        update_disciplina(row["id_disciplina"], nombre, descripcion)
                        st.rerun()

        st.divider()

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
                create_docente(nombre, apellido, correo, telefono)
                st.rerun()

    df_docentes = read_docentes()

    for index, row in df_docentes.iterrows():
        st.subheader(f"{row['nombre']} {row['apellido']}")
        st.write(f"Correo: {row['correo']}")
        st.write(f"Teléfono: {row['telefono']}")

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_docente_{row['id_docente']}"):
                delete_docente(row["id_docente"])
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
                        update_docente(row["id_docente"], nombre, apellido, correo, telefono)
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
                create_representante(nombre, telefono, correo, clausulas)
                st.rerun()

    df_representantes = read_representantes()

    for index, row in df_representantes.iterrows():
        st.subheader(row["nombre"])
        st.write(f"Teléfono: {row['telefono']}")
        st.write(f"Correo: {row['correo']}")
        st.write(f"Cláusulas: {row['clausulas']}")

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_representante_{row['id_representante']}"):
                delete_representante(row["id_representante"])
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
                        update_representante(row["id_representante"], nombre, telefono, correo, clausulas)
                        st.rerun()

        st.divider()

with tab4:
    st.header("Academias")

    with st.expander("Crear nueva academia"):
        with st.form("crear_academia_form"):
            categoria = st.text_input("Categoría")
            n_estudiantes = st.number_input("Número de estudiantes", min_value=0, step=1)
            fecha_creacion = st.date_input("Fecha de creación")
            descripcion = st.text_area("Descripción")
            periodo = st.text_input("Periodo")
            
            df_disciplinas = read_disciplinas()
            disciplina_options = {row["nombre"]: row["id_disciplina"] for index, row in df_disciplinas.iterrows()}
            selected_disciplina_nombre = st.selectbox("Disciplina", options=list(disciplina_options.keys()))
            
            submitted = st.form_submit_button("Crear")
            if submitted:
                id_disciplina = disciplina_options[selected_disciplina_nombre]
                create_academia(categoria, n_estudiantes, fecha_creacion, descripcion, id_disciplina, periodo)
                st.rerun()

    df_academias = read_academias()

    for index, row in df_academias.iterrows():
        st.subheader(row["categoria"])
        st.write(f"Número de estudiantes: {row['n_estudiantes']}")
        st.write(f"Fecha de creación: {row['fecha_creacion']}")
        st.write(f"Descripción: {row['descripcion']}")
        st.write(f"Periodo: {row['periodo']}")
        
        df_disciplina = read_disciplinas()
        disciplina_nombre = df_disciplina[df_disciplina["id_disciplina"] == row["id_disciplina"]]["nombre"].iloc[0]
        st.write(f"Disciplina: {disciplina_nombre}")


        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_academia_{row['id_academia']}"):
                delete_academia(row["id_academia"])
                st.rerun()
        
        with col2:
            with st.expander("Editar"):
                with st.form(f"editar_academia_form_{row['id_academia']}"):
                    categoria = st.text_input("Categoría", value=row["categoria"], key=f"edit_categoria_academia_{row['id_academia']}")
                    n_estudiantes = st.number_input("Número de estudiantes", value=row["n_estudiantes"], min_value=0, step=1, key=f"edit_n_estudiantes_academia_{row['id_academia']}")
                    fecha_creacion = st.date_input("Fecha de creación", value=pd.to_datetime(row["fecha_creacion"]), key=f"edit_fecha_creacion_academia_{row['id_academia']}")
                    descripcion = st.text_area("Descripción", value=row["descripcion"], key=f"edit_desc_academia_{row['id_academia']}")
                    periodo = st.text_input("Periodo", value=row["periodo"], key=f"edit_periodo_academia_{row['id_academia']}")

                    df_disciplinas = read_disciplinas()
                    disciplina_options = {row_disp["nombre"]: row_disp["id_disciplina"] for index_disp, row_disp in df_disciplinas.iterrows()}
                    
                    current_disciplina_nombre = df_disciplina[df_disciplina["id_disciplina"] == row["id_disciplina"]]["nombre"].iloc[0]
                    
                    disciplina_list = list(disciplina_options.keys())
                    current_disciplina_index = disciplina_list.index(current_disciplina_nombre)

                    selected_disciplina_nombre = st.selectbox("Disciplina", options=disciplina_list, index=current_disciplina_index, key=f"edit_disciplina_academia_{row['id_academia']}")
                    
                    submitted = st.form_submit_button("Actualizar")
                    if submitted:
                        id_disciplina = disciplina_options[selected_disciplina_nombre]
                        update_academia(row["id_academia"], categoria, n_estudiantes, fecha_creacion, descripcion, id_disciplina, periodo)
                        st.rerun()

        st.divider()

with tab5:
    st.header("Estudiantes")

    with st.expander("Crear nuevo estudiante"):
        with st.form("crear_estudiante_form"):
            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido")
            promedio = st.number_input("Promedio", min_value=0.0, max_value=10.0, step=0.1)
            fecha_nac = st.date_input("Fecha de nacimiento")
            correo = st.text_input("Correo")
            curso = st.text_input("Curso")

            df_representantes = read_representantes()
            representante_options = {row["nombre"]: row["id_representante"] for index, row in df_representantes.iterrows()}
            selected_representante_nombre = st.selectbox("Representante", options=list(representante_options.keys()))

            df_academias = read_academias()
            academia_options = {row["categoria"]: row["id_academia"] for index, row in df_academias.iterrows()}
            selected_academia_nombre = st.selectbox("Academia", options=list(academia_options.keys()))
            
            submitted = st.form_submit_button("Crear")
            if submitted:
                id_representante = representante_options[selected_representante_nombre]
                id_academia = academia_options[selected_academia_nombre]
                create_estudiante(id_representante, id_academia, nombre, promedio, fecha_nac, correo, curso, apellido)
                st.rerun()

    df_estudiantes = read_estudiantes()

    for index, row in df_estudiantes.iterrows():
        st.subheader(f"{row['nombre']} {row['apellido']}")
        st.write(f"Promedio: {row['promedio']}")
        st.write(f"Fecha de nacimiento: {row['fecha_nac']}")
        st.write(f"Correo: {row['correo']}")
        st.write(f"Curso: {row['curso']}")

        df_representante = read_representantes()
        representante_nombre = df_representante[df_representante["id_representante"] == row["id_representante"]]["nombre"].iloc[0]
        st.write(f"Representante: {representante_nombre}")

        df_academia = read_academias()
        academia_nombre = df_academia[df_academia["id_academia"] == row["id_academia"]]["categoria"].iloc[0]
        st.write(f"Academia: {academia_nombre}")

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_estudiante_{row['id_estudiante']}"):
                delete_estudiante(row["id_estudiante"])
                st.rerun()

        with col2:
            with st.expander("Editar"):
                with st.form(f"editar_estudiante_form_{row['id_estudiante']}"):
                    nombre = st.text_input("Nombre", value=row["nombre"], key=f"edit_nombre_estudiante_{row['id_estudiante']}")
                    apellido = st.text_input("Apellido", value=row["apellido"], key=f"edit_apellido_estudiante_{row['id_estudiante']}")
                    promedio = st.number_input("Promedio", value=row["promedio"], min_value=0.0, max_value=10.0, step=0.1, key=f"edit_promedio_estudiante_{row['id_estudiante']}")
                    fecha_nac = st.date_input("Fecha de nacimiento", value=pd.to_datetime(row["fecha_nac"]), key=f"edit_fecha_nac_estudiante_{row['id_estudiante']}")
                    correo = st.text_input("Correo", value=row["correo"], key=f"edit_correo_estudiante_{row['id_estudiante']}")
                    curso = st.text_input("Curso", value=row["curso"], key=f"edit_curso_estudiante_{row['id_estudiante']}")

                    df_representantes = read_representantes()
                    representante_options = {row_rep["nombre"]: row_rep["id_representante"] for index_rep, row_rep in df_representantes.iterrows()}
                    current_representante_nombre = df_representante[df_representante["id_representante"] == row["id_representante"]]["nombre"].iloc[0]
                    representante_list = list(representante_options.keys())
                    current_representante_index = representante_list.index(current_representante_nombre)
                    selected_representante_nombre = st.selectbox("Representante", options=representante_list, index=current_representante_index, key=f"edit_representante_estudiante_{row['id_estudiante']}")

                    df_academias = read_academias()
                    academia_options = {row_aca["categoria"]: row_aca["id_academia"] for index_aca, row_aca in df_academias.iterrows()}
                    current_academia_nombre = df_academia[df_academia["id_academia"] == row["id_academia"]]["categoria"].iloc[0]
                    academia_list = list(academia_options.keys())
                    current_academia_index = academia_list.index(current_academia_nombre)
                    selected_academia_nombre = st.selectbox("Academia", options=academia_list, index=current_academia_index, key=f"edit_academia_estudiante_{row['id_estudiante']}")

                    submitted = st.form_submit_button("Actualizar")
                    if submitted:
                        id_representante = representante_options[selected_representante_nombre]
                        id_academia = academia_options[selected_academia_nombre]
                        update_estudiante(row["id_estudiante"], id_representante, id_academia, nombre, promedio, fecha_nac, correo, curso, apellido)
                        st.rerun()

        st.divider()

with tab6:
    st.header("Entrenadores")

    with st.expander("Crear nuevo entrenador"):
        with st.form("crear_entrenador_form"):
            df_docentes = read_docentes()
            docente_options = {f"{row['nombre']} {row['apellido']}": row["id_docente"] for index, row in df_docentes.iterrows()}
            selected_docente_nombre = st.selectbox("Docente", options=list(docente_options.keys()))

            df_academias = read_academias()
            academia_options = {row["categoria"]: row["id_academia"] for index, row in df_academias.iterrows()}
            selected_academia_nombre = st.selectbox("Academia", options=list(academia_options.keys()))
            
            submitted = st.form_submit_button("Crear")
            if submitted:
                id_docente = docente_options[selected_docente_nombre]
                id_academia = academia_options[selected_academia_nombre]
                create_entrenador(id_docente, id_academia)
                st.rerun()

    df_entrenadores = read_entrenadores()

    for index, row in df_entrenadores.iterrows():
        df_docente = read_docentes()
        docente_nombre = df_docente[df_docente["id_docente"] == row["id_docente"]]["nombre"].iloc[0]
        docente_apellido = df_docente[df_docente["id_docente"] == row["id_docente"]]["apellido"].iloc[0]
        st.subheader(f"Entrenador: {docente_nombre} {docente_apellido}")

        df_academia = read_academias()
        academia_nombre = df_academia[df_academia["id_academia"] == row["id_academia"]]["categoria"].iloc[0]
        st.write(f"Academia: {academia_nombre}")

        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            if st.button("Eliminar", key=f"delete_entrenador_{row['id_entrenador']}"):
                delete_entrenador(row["id_entrenador"])
                st.rerun()

        with col2:
            with st.expander("Editar"):
                with st.form(f"editar_entrenador_form_{row['id_entrenador']}"):
                    df_docentes = read_docentes()
                    docente_options = {f"{row_doc['nombre']} {row_doc['apellido']}": row_doc["id_docente"] for index_doc, row_doc in df_docentes.iterrows()}
                    current_docente_nombre = f"{docente_nombre} {docente_apellido}"
                    docente_list = list(docente_options.keys())
                    current_docente_index = docente_list.index(current_docente_nombre)
                    selected_docente_nombre = st.selectbox("Docente", options=docente_list, index=current_docente_index, key=f"edit_docente_entrenador_{row['id_entrenador']}")

                    df_academias = read_academias()
                    academia_options = {row_aca["categoria"]: row_aca["id_academia"] for index_aca, row_aca in df_academias.iterrows()}
                    current_academia_nombre = df_academia[df_academia["id_academia"] == row["id_academia"]]["categoria"].iloc[0]
                    academia_list = list(academia_options.keys())
                    current_academia_index = academia_list.index(current_academia_nombre)
                    selected_academia_nombre = st.selectbox("Academia", options=academia_list, index=current_academia_index, key=f"edit_academia_entrenador_{row['id_entrenador']}")

                    submitted = st.form_submit_button("Actualizar")
                    if submitted:
                        id_docente = docente_options[selected_docente_nombre]
                        id_academia = academia_options[selected_academia_nombre]
                        update_entrenador(row["id_entrenador"], id_docente, id_academia)
                        st.rerun()

        st.divider()
