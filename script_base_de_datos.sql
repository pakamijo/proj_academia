create database academiasComboni;
use academiasComboni;

create table disciplina(
id_disciplina int auto_increment,
nombre varchar(50) not null unique,
descripcion varchar (50),
primary key(id_disciplina)
);

create table academia(
id_academia int auto_increment,
categoria varchar(50) not null,
n_estudiantes int,
fecha_creacion date,
descripcion varchar(255),
id_disciplina int not null,
periodo varchar(100),

primary key(id_academia),
foreign key(id_disciplina) references disciplina(id_disciplina)
);

create table entrenamiento(
id_entrenamiento int auto_increment,
id_academia int not null,
horario varchar(100) not null,
horario_2 varchar(100),
horario_3 varchar(100),

primary key(id_entrenamiento),
foreign key(id_academia) references academia(id_academia)
on delete cascade
);

create table competencia(
id_competencia int auto_increment,
id_academia int not null,
nombre_competencia varchar(100) not null,
fecha date not null,
lugar_competencia varchar(100),
resultado varchar(100),

primary key(id_competencia),
foreign key(id_academia) references academia(id_academia)
on delete cascade
);

create table representante(
id_representante int auto_increment,
nombres varchar(100) not null,
apellidos varchar(100) not null,
telefono varchar(10),
correo varchar(100),
clausulas varchar(100),

primary key(id_representante)
);

create table estudiante(
id_estudiante int auto_increment,
id_representante int not null,
id_academia int not null,
nombres varchar(100) not null,
apellidos varchar(100) not null,
promedio float not null,
fecha_nac date,
correo varchar(100),
curso varchar(100),

primary key(id_estudiante),
foreign key(id_representante) references representante(id_representante),
foreign key(id_academia) references academia(id_academia)
);

create table pago(
id_pago int auto_increment,
id_representante int not null,
id_academia int not null,
fecha_pago date not null,
monto float not null,
periodo varchar(100),

primary key(id_pago),
foreign key(id_representante) references representante(id_representante),
foreign key(id_academia) references academia(id_academia)
);

create table docente(
id_docente int auto_increment,
nombres varchar(100) not null,
apellidos varchar(100) not null,
correo varchar(100) not null,
telefono varchar(10) not null,

primary key(id_docente)
);

create table curso(
id_curso int auto_increment,
id_docente int not null,
curso varchar(100) not null,

primary key (id_curso),
foreign key(id_docente) references docente(id_docente)
);

create table materia(
id_materia int auto_increment,
materia varchar(100),

primary key(id_materia)
);

create table docente_materia(
	id_docente int not null,
    id_materia int not null,
    
    primary key(id_docente, id_materia),
    foreign key(id_docente) references docente(id_docente),
    foreign key(id_materia) references materia(id_materia)
);

create table entrenador(
id_entrenador int auto_increment,
id_docente int not null,
id_academia int not null,

primary key(id_entrenador),
foreign key(id_docente) references docente(id_docente),
foreign key(id_academia) references academia(id_academia)
);

create table coordinador(
id_coordinador int auto_increment,
id_docente int not null,
id_academia int not null,

primary key(id_coordinador),
foreign key(id_docente) references docente(id_docente),
foreign key(id_academia) references academia(id_academia)
);