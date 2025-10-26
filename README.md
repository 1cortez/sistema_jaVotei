## 📝 Introdução ao projeto

O sistema JáVotei foi desenvolvido como parte da disciplina Banco de Dados do curso de Gestão de Dados da Universidade Federal do Piauí (UFPI).
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

#### 👉 Script completo de criação das tabelas:
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
  
#### Povoamento da tabela (usuario) :
```sql
INSERT INTO usuario (id_usuario, usuario, email, senha)
VALUES
(02, 'qmendonca', 'maria-fernanda39@example.net', '%44+iZs#'),
(03, 'cauajesus', 'vitor-gabriel59@example.net', 'h)J71nSgf'),
(04, 'portogael', 'usilveira@example.net', 'a@0WJa'),
(05, 'zda-cruz', 'dmoura@example.com', 'm^64YkY'),
(06, 'ayllamachado', 'pintomaria-laura@example.com', 'VG08PgUo$c'),
(07, 'da-luzmaria-eduarda', 'ana-lauraborges@example.com', 'P+4Wr!'),
(08, 'beatrizoliveira', 'riosbruna@example.org', 'e(1DQqUi1'),
(09, 'oda-cunha', 'leticia87@example.com', '5dgSv&YV*&4'),
(10, 'davi-lucca95', 'valentimnogueira@example.com', '8Nay5IOakm&i'),
(11, 'raulda-paz', 'rmelo@example.org', '*Yy1EUeii'),
(12, 'hcavalcante', 'kamillyfogaca@example.com', '5+7#qFpL^'),
(13, 'joao-vitor91', 'casa-grandelunna@example.com', ')5$RaU'),
(14, 'doliveira', 'montenegrojuliana@example.net', '_8Wbqi'),
(15, 'britocaua', 'oliver53@example.com', ')+4rLdGUfjxV'),
(16, 'baparecida', 'ravi-lucca96@example.com', 'bqhV0RxJ$R'),
(17, 'augustoandrade', 'avieira@example.org', '_H(3Nfs'),
(18, 'kcassiano', 'da-cunhagabriel@example.org', '@pVg3WHC0'),
(19, 'henry33', 'noahporto@example.net', '+R0En2e&H&A'),
(20, 'ncampos', 'maria-luiza91@example.net', '*4lTHiIl!'),
(21, 'rioshenrique', 'luiz-otavioandrade@example.net', '&78%fSrn');
```

- Criação e povoamento do banco de dados.
- Consultas SQL (com agregações, junções e ordenações).



## 👨‍💻 Parte 3 – Aplicação Prática (Python + Tkinter e SQLite3)

  - Tela de login com validação de acesso :
  <img width="641" height="681" alt="Screenshot_16" src="https://github.com/user-attachments/assets/54e1feea-3fc4-474c-b67e-f08ec249294a" />

  - Tela de seleção entre criar um grupo e entrar em um :
<img width="701" height="699" alt="Screenshot_17" src="https://github.com/user-attachments/assets/c745369e-41b5-4aef-9e35-2dcb54dc5568" />

- Tela de votação de jogos :
<img width="683" height="660" alt="Screenshot_18" src="https://github.com/user-attachments/assets/140f897e-75f4-488e-a372-6b38d06d3892" />

* Tecnologias utilizadas : Python + Tkinter e SQLite3
    



---
**Autor:** Guilherme Francisco França Cortez  
**Disciplina:** Banco de Dados  
**Instituição:** UFPI  
