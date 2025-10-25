## 📝 Introdução do projeto

O projeto JáVotei foi desenvolvido como parte da disciplina Banco de Dados do curso de Gestão de Dados da Universidade Federal do Piauí (UFPI).
Seu objetivo é aplicar de forma prática os conceitos de modelagem relacional, implementação de bancos de dados e execução de consultas SQL utilizando o PostgreSQL.

O sistema simula um ambiente de votação de jogos eletrônicos, permitindo o cadastro de usuários, criação de grupos, votação e avaliação de jogos, além da execução de consultas envolvendo junções, agregações e ordenações.

O projeto foi dividido em três partes principais:

Modelagem Lógica (DER) – elaboração do diagrama entidade-relacionamento e definição das chaves e relacionamentos;

Implementação em PostgreSQL – criação das tabelas, povoamento do banco e desenvolvimento das consultas SQL;

Aplicação Prática (Python + Tkinter) – desenvolvimento de uma interface gráfica funcional para demonstrar o funcionamento do sistema de votação na prática.

## 📘 Parte 1 – Modelagem de banco de dados conceitual (DER)
- Diagrama entidade-relacionamento com explicação detalhada.
 <img width="757" height="494" alt="Screenshot_97" src="https://github.com/user-attachments/assets/f1f317b9-8e97-49d8-a564-2f0215198212" />

#### **Entidades e Atributos:**

- **Usuário**: Responsável pelo cadastro na plataforma, podendo criar ou participar de grupos.  
  **Atributos**: `ID_Usuário`, `Nome`, `E-mail`, `Senha`.

- **Grupo**: Criado por usuários e destinado à organização dos membros.  
  **Atributos**: `ID_Grupo`, `Nome do Grupo`, `Descrição`.

- **Jogo**: Representa os jogos cadastrados no sistema.  
  **Atributos**: `ID_Jogo`, `Nome`, `Gênero`, `Plataforma`.

- **Votação**: Processo em que os membros de um grupo escolhem, entre os jogos cadastrados, qual será selecionado para jogar.

---

### 🔗 **Relacionamentos:**

- Um **Usuário** pode **criar vários Grupos** → (1:N).
- Um **Usuário** pode **participar de vários Grupos**, e cada Grupo pode ter vários Usuários → (N:N).
- Um **Grupo** realiza **uma única Votação** → (1:1).
- Uma **Votação** permite escolher entre **vários Jogos** → (N:N).

---


## 🧮 Parte 2 – Modelo Lógico DBDesigner + Implementação em PostgreSQL
#### Modelo lógico no DBDesginer
  <img width="1624" height="898" alt="Screenshot_11" src="https://github.com/user-attachments/assets/1685e255-6728-4221-8a8f-e2662554f116" />

#### 👉 script completo de criação das tabelas:
```sql
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
```


#### 🐍Algoritmo para gerar dados para popular o banco de dados (via Python + Faker).
```python
from faker import Faker
import random

fake = Faker('pt_BR')
usuarios = []

for _ in range(20):  
    nome = fake.user_name()
    email = fake.email()
    senha = fake.password(length=random.randint(6, 12))
    usuarios.append((nome, email, senha))

for nome, email, senha in usuarios:
    print(f'nome : {nome} , email : {email}, senha : {senha}', end=' ')
    print()
```
  

- Criação e povoamento do banco de dados.
- Consultas SQL (com agregações, junções e ordenações).



## 👨‍💻 Parte 3 – Aplicação Prática (Python + Tkinter)



---
**Autor:** Guilherme Francisco França Cortez  
**Disciplina:** Banco de Dados  
**Instituição:** UFPI  
