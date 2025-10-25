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
- Modelo lógico no DBDesginer
  <img width="1624" height="898" alt="Screenshot_11" src="https://github.com/user-attachments/assets/1685e255-6728-4221-8a8f-e2662554f116" />
## 🗄️ Script de Criação das Tabelas
Você pode acessar o script completo de criação das tabelas clicando no link abaixo:

👉 Visualizar script.sql

- Algoritmo de exemplo para gerar dados para popular o banco de dados (via Python + Faker).
  <img width="755" height="386" alt="Screenshot_14" src="https://github.com/user-attachments/assets/176f9bc1-4aff-4a87-ba04-4b2634c1232f" />

  

- Criação e povoamento do banco de dados.
- Consultas SQL (com agregações, junções e ordenações).



## 👨‍💻 Parte 3 – Aplicação Prática (Python + Tkinter)



---
**Autor:** Guilherme Francisco França Cortez  
**Disciplina:** Banco de Dados  
**Instituição:** UFPI  
