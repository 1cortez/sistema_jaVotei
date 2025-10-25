from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

class Funcs:

    def conectar_bd(self):
        self.conn = sqlite3.connect('dados_usuarios.bd')
        self.cursor = self.conn.cursor()
    
    def desconectar(self):
        self.conn.close(); print('Desconectado!')
    
    def montarTabelas(self):
        self.conectar_bd() #conectar bd
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            usuario VARCHAR(30) PRIMARY KEY,
                            email VARCHAR(60) NOT NULL,
                            senha VARCHAR(60) NOT NULL
                            )
                            ''')
        
        self.conn.commit(); print('Banco criado')
        self.desconectar()
    
    def cadastrar_usuario(self, usuario, email, senha):
        self.conectar_bd()
        try:
            self.cursor.execute("""
                INSERT INTO clientes (usuario, email, senha)
                VALUES (?, ?, ?)
                """, (usuario, email, senha))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        except sqlite3.IntegrityError:
            messagebox.showwarning("Erro", "Usuário já existe!")
        finally:
            self.desconectar()
        
    def salvar_cadastro(self):
        usuario = self.input_entry.get()
        email = self.input_email.get()
        senha = self.input_senha.get()

        if not usuario or not email or not senha:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        self.cadastrar_usuario(usuario, email, senha)

        # limpa os campos
        self.input_entry.delete(0, END)
        self.input_email.delete(0, END)
        self.input_senha.delete(0, END)

        # volta pra tela de login
        self.frame_2.destroy()
        TelaLogin()
        


class TelaLogin(Funcs):
    def __init__(self):
        self.root = root
        self.tela_main()
        self.frames()
        self.botoes()
        
    def tela_main(self):
        self.root.title('Tela de Login')
        self.root.configure(bg='lightgray')
        self.root.geometry('600x600') 
        
    def frames(self):
        self.frame_1 = Frame(self.root, bg='#E3E1E1', width=500, height=450, highlightbackground='#2761F5', highlightthickness=3)
        self.frame_1.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento
    
    def botoes(self):
        self.bt_logar = Button(self.frame_1, text='LOGIN', background='#2761F5', font=('Arial', 9, 'bold'), command=self.validar_login, fg='white')
        self.bt_logar.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.06)

        self.bt_cadastrar = Button(self.frame_1, text='Cadastre-se', font=('Arial', 10, 'bold'), command=self.abrir_cadastro)
        self.bt_cadastrar.place(relx=0.54, rely=0.8, relheight=0.05, relwidth=0.2)

        # criação da label e entrada do código
        self.lb_text = Label(self.frame_1, text='JáVotei!', font=('Arial', 19, 'bold'), bg='#E3E1E1')
        self.lb_text.place(relx=0.5, rely=0.05, anchor=N)

        self.lb_cadastro = Label(self.frame_1, text='Ainda não tem conta?', font=('Arial', 9, 'bold'), bg='#E3E1E1' )
        self.lb_cadastro.place(relx=0.4, rely=0.85, anchor=S)

        self.lb_user = Label(self.frame_1)

        # metodo input do tkinter
        self.input_entry = Entry(self.frame_1, highlightbackground='#2761F5', highlightthickness=1)
        self.input_entry.place(relx=0.2, rely=0.4, relheight=0.06, relwidth=0.6)
        
        self.input_senha = Entry(self.frame_1, highlightbackground='#2761F5', highlightthickness=1, show='*')
        self.input_senha.place(relx=0.2, rely=0.55, relheight=0.06, relwidth=0.6)

        self.lb_user = Label(self.frame_1, text='Usuário', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_user.place(relx=0.21, rely=0.33)

        self.lb_senha = Label(self.frame_1, text='Senha', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_senha.place(relx=0.21, rely=0.48)

    def validar_login(self):
        usuario = self.input_entry.get()
        senha = self.input_senha.get()

        self.conectar_bd()
        self.cursor.execute("SELECT * FROM clientes WHERE usuario=? AND senha=?", (usuario, senha))
        resultado = self.cursor.fetchone()
        self.desconectar()

        if resultado:
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.abrir_votacao()
        else:
            messagebox.showwarning("Erro", "Usuário ou senha incorretos!")        

    def abrir_cadastro(self):
        self.frame_1.destroy()  # Remove a tela de login
        Cadastro(self.root)     # Abre a tela de cadastro

    def abrir_votacao(self):
        self.frame_1.destroy() # Remove a tela de login    
        Votacao(self.root) # Abre a tela de cadastro

class Cadastro(Funcs):
    
    def __init__(self, root):
        self.root = root
        self.tela_cadastro()
        self.frames()
        self.botoes()
        self.montarTabelas()
    
    def tela_cadastro(self):
        self.root.title('Tela de cadastro')
        self.root.configure(bg='lightgray')
        self.root.geometry('600x600')
    
    def frames(self):
        self.frame_2 = Frame(self.root, bg='#E3E1E1', width=500, height=450, highlightbackground='#2761F5', highlightthickness=3)
        self.frame_2.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento
    
    def botoes(self):
        self.bt_inscrever = Button(self.frame_2, text='INSCREVER-SE', command=self.salvar_cadastro, background='#2761F5', font=('Arial', 10, 'bold'), fg='white')
        self.bt_inscrever.place(relx=0.5, rely=0.74, relwidth=0.3, relheight=0.06, anchor=CENTER)

        self.bt_voltar = Button(self.frame_2, text='VOLTAR', command=self.abrir_login, background='#2761F5', font=('Arial', 10, 'bold'), fg='white')
        self.bt_voltar.place(relx=0.5, rely=0.83, relwidth=0.3, relheight=0.06, anchor=CENTER)

        self.lb_cadastro = Label(self.frame_2, text='Cadastro', font=('Arial', 19, 'bold'), bg='#E3E1E1')
        self.lb_cadastro.place(relx=0.5, rely=0.05, anchor=N)

        # cadastro do user

        self.input_entry = Entry(self.frame_2, highlightbackground='#2761F5', highlightthickness=1)
        self.input_entry.place(relx=0.2, rely=0.29, relheight=0.06, relwidth=0.6)
        
        self.input_email = Entry(self.frame_2, highlightbackground='#2761F5', highlightthickness=1)
        self.input_email.place(relx=0.2, rely=0.43, relheight=0.06, relwidth=0.6)
        
        self.input_senha = Entry(self.frame_2, highlightbackground='#2761F5', highlightthickness=1, show='*')
        self.input_senha.place(relx=0.2, rely=0.58, relheight=0.06, relwidth=0.6)

        self.lb_user = Label(self.frame_2, text='Usuário', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_user.place(relx=0.21, rely=0.22)

        self.lb_email = Label(self.frame_2, text='E-mail', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_email.place(relx=0.21, rely=0.36)

        self.lb_senha = Label(self.frame_2, text='Senha', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_senha.place(relx=0.21, rely=0.51)

    def abrir_login(self):
        #messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")  # <- mensagem
        self.frame_2.destroy()  # Remove a tela de cadastro
        TelaLogin()     # Abre a tela de login
    
class Votacao(Funcs):
    def __init__(self, root):
        self.root = root
        self.tela_main_2()
        self.frames()
        self.botoes()

    def tela_main_2(self):
        self.root.title('Tela de votação')
        self.root.configure(background='lightgray')
        self.root.geometry('600x600')

    def frames(self):
        self.frame_3 = Frame(self.root, bg='#E3E1E1', width=500, height=450, highlightbackground='#2761F5', highlightthickness=3)
        self.frame_3.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento
    
    def botoes(self):
        self.bt_criar = Button(self.frame_3, text='Criar Grupo', bg='#2761F5', font=('Arial', 12, 'bold'), fg='white', command=self.abrir_criar_grupo)
        self.bt_criar.place(relx=0.5, rely=0.4, anchor='center', relheight=0.12, relwidth=0.3)
        
        self.bt_entrar = Button(self.frame_3, text='Entrar em Grupo', bg='#2761F5', font=('Arial', 12, 'bold'), fg='white', command=self.abrir_entrar_grupo)
        self.bt_entrar.place(relx=0.5, rely=0.55, anchor='center', relheight=0.12, relwidth=0.3)

        self.bt_sair = Button(self.frame_3, text='Sair', font=('Arial', 12, 'bold'), command=self.abrir_login)
        self.bt_sair.place(relx=0.5, rely=0.9, anchor=S, relheight=0.12, relwidth=0.3)

        # label do código
        self.lb_votacoes = Label(self.frame_3, text='Selecione uma opção', font=('Arial', 19, 'bold'), bg='#E3E1E1')
        self.lb_votacoes.place(relx=0.5, rely=0.05, anchor=N)

    def abrir_login(self):
        self.frame_3.destroy()  # Remove a tela de cadastro
        TelaLogin()     # Abre a tela de login
    
    def abrir_criar_grupo(self):
        self.frame_3.destroy()
        Criar_grupo(self.root)
    
    def abrir_entrar_grupo(self):
        self.frame_3.destroy()
        Entrar_grupo(self.root)
    
class Criar_grupo(Funcs):
    def __init__(self, root):
        self.root = root
        self.tela_criar_grupo()
        self.frames()
        self.botoes()
        
    def tela_criar_grupo(self):
        self.root.title('Criação de grupo')
        self.root.configure(background='lightgray')
        self.root.geometry('600x600')
    
    def frames(self):
        self.frame_4 = Frame(self.root, bg='#E3E1E1', width=500, height=450, highlightbackground='#2761F5', highlightthickness=3)
        self.frame_4.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento
    
    def botoes(self):
        self.bt_criar = Button(self.frame_4, text='Criar Grupo', bg='#2761F5', font=('Arial', 12, 'bold'), fg='white', command=self.abrir_votar_jogo)
        self.bt_criar.place(relx=0.5, rely=0.6, anchor='center', relheight=0.12, relwidth=0.3)

        # input para o botao criar
        self.input_grupo = Entry(self.frame_4, highlightbackground='#2761F5', highlightthickness=1)
        self.input_grupo.place(relx=0.5, rely=0.38, relheight=0.06, relwidth=0.6, anchor=CENTER)

        # label 
        self.lb_insira = Label(self.frame_4, text='Insira o nome do grupo : ', font=('Arial', 19, 'bold'), bg='#E3E1E1')
        self.lb_insira.place(relx=0.5, rely=0.05, anchor=N)
    
    def abrir_votar_jogo(self):
        messagebox.showinfo("Sucesso", "Grupo criado com sucesso!")
        self.frame_4.destroy()
        Votar_Jogo(self.root)
    
class Entrar_grupo(Funcs):
    
    def __init__(self, root):
        self.root = root
        self.janela()
        self.frames()
    
    def janela(self):
        self.root.title('Entrar em um grupo')
        self.root.configure(background='lightgray')
        self.root.geometry('600x600')
    
    def frames(self):
        self.frame_5 = Frame(self.root, bg='#E3E1E1', width=500, height=450, highlightbackground='#2761F5', highlightthickness=3)
        self.frame_5.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    def abrir_votar_jogo(self):
        messagebox.showinfo("Sucesso", "Entrada no grupo realizada com sucesso!")
        self.frame_5.destroy()
        Votar_Jogo(self.root)

class Votar_Jogo(Funcs):
    
    def __init__(self, root):
        self.root = root
        self.janela()
        self.frames()
        self.botoes()
    
    def janela(self):
        self.root.title('Votar em um jogo')
        self.root.configure(background='lightgray')
        self.root.geometry('600x600')
    
    def frames(self):
        self.frame_6 = Frame(self.root, bg='#E3E1E1', width=500, height=450, highlightbackground='#2761F5', highlightthickness=3)
        self.frame_6.place(relx=0.5, rely=0.5, anchor=CENTER)

    def botoes(self):
        self.lb_insira = Label(self.frame_6, text='Vote em um jogo : ', font=('Arial', 19, 'bold'), bg='#E3E1E1')
        self.lb_insira.place(relx=0.5, rely=0.05, anchor=N)

        self.bt_voto = Checkbutton(self.frame_6, text="FORTNITE", bg='#E3E1E1', font=('Arial', 9, 'bold'))
        self.bt_voto.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        self.bt_voto_1 = Checkbutton(self.frame_6, text="EAFC 25", bg='#E3E1E1', font=('Arial', 9, 'bold'))
        self.bt_voto_1.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.bt_voto_2 = Checkbutton(self.frame_6, text="COUNTER STRIKE 2", bg='#E3E1E1', font=('Arial', 9, 'bold'))
        self.bt_voto_2.place(relx=0.5, rely=0.6, anchor=CENTER)

class Ver_votos(Funcs):
    
    def __init__(self, root):
        self.root = root
        self.janela()
        self.frames()
    
    def janela(self):
        self.root.title('Votar em um jogo')
        self.root.configure(background='lightgray')
        self.root.geometry('600x600')
    
    def frames(self):
        self.frame_7 = Frame(self.root, bg='#E3E1E1', width=500, height=450, highlightbackground='#2761F5', highlightthickness=3)
        self.frame_7.place(relx=0.5, rely=0.5, anchor=CENTER)

        #label
        self.lb_insira = Label(self.frame_7, text='Votos em tempo real : ', font=('Arial', 19, 'bold'), bg='#E3E1E1')
        self.lb_insira.place(relx=0.5, rely=0.05, anchor=N)
    
    def botoes(self):
        Checkbutton(self.frame_7, text="Opção 1", variable=self.opcao1).pack(anchor='w', padx=20)
    




TelaLogin()
root.mainloop()

