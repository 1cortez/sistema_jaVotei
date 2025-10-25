CREATE TABLE IF NOT EXISTS Usuario (
	id_usuario serial NOT NULL UNIQUE,
	usuario varchar(30) NOT NULL,
	email varchar(100) NOT NULL,
	senha varchar(50) NOT NULL,
	PRIMARY KEY (id_usuario)
);

CREATE TABLE IF NOT EXISTS GRUPO (
	id_grupo serial NOT NULL UNIQUE,
	nome_grupo varchar(20) NOT NULL,
	PRIMARY KEY (id_grupo)
);

CREATE TABLE IF NOT EXISTS VOTACAO (
	id_votacao serial NOT NULL UNIQUE,
	id_grupo bigint NOT NULL,
	PRIMARY KEY (id_votacao)
);

CREATE TABLE IF NOT EXISTS JOGO (
	id_jogo serial NOT NULL UNIQUE,
	nome varchar(255) NOT NULL,
	genero varchar(255) NOT NULL,
	plataforma varchar(255),
	PRIMARY KEY (id_jogo)
);

CREATE TABLE IF NOT EXISTS Usuario_grupo (
	id_usuario bigint NOT NULL,
	id_grupo bigint NOT NULL,
	PRIMARY KEY (id_usuario, id_grupo)
);

CREATE TABLE IF NOT EXISTS Avaliacao (
	id_avaliacao serial NOT NULL UNIQUE,
	id_usuario bigint NOT NULL,
	id_jogo bigint NOT NULL,
	nota bigint NOT NULL,
	PRIMARY KEY (id_avaliacao)
);

CREATE TABLE IF NOT EXISTS Votacao_Jogo (
	id_votacao bigint NOT NULL,
	id_jogo bigint NOT NULL,
	PRIMARY KEY (id_votacao, id_jogo)
);



ALTER TABLE VOTACAO ADD CONSTRAINT VOTACAO_fk1 FOREIGN KEY (id_grupo) REFERENCES GRUPO(id_grupo);

ALTER TABLE Usuario_grupo ADD CONSTRAINT Usuario_grupo_fk0 FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario);

ALTER TABLE Usuario_grupo ADD CONSTRAINT Usuario_grupo_fk1 FOREIGN KEY (id_grupo) REFERENCES GRUPO(id_grupo);
ALTER TABLE Avaliacao ADD CONSTRAINT Avaliacao_fk1 FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario);

ALTER TABLE Avaliacao ADD CONSTRAINT Avaliacao_fk2 FOREIGN KEY (id_jogo) REFERENCES JOGO(id_jogo);
ALTER TABLE Votacao_Jogo ADD CONSTRAINT Votacao_Jogo_fk0 FOREIGN KEY (id_votacao) REFERENCES VOTACAO(id_votacao);

ALTER TABLE Votacao_Jogo ADD CONSTRAINT Votacao_Jogo_fk1 FOREIGN KEY (id_jogo) REFERENCES JOGO(id_jogo);
