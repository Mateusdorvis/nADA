import tkinter as tk
from datetime import datetime
from elementos_tkinter import Buttoncustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Textcustomizado
from sistema_login import Registro, Login
from modelo import SalvarUsuario, CarregarUsuario

class Controle:
    def __init__(self, root):
        self.root = root
        self.contar_click = 0
        self.registro = Registro(self.root)
        self.config_button_enviar()
        self.config_check()
        self.config_eventos()
    
    def abrir_janela_registro(self):
        self.window.destroy()  # Fechar a janela de login
        self.registro.abrir()  # Mostrar a janela de registro

    def abrir_janela_login(self):
        def check_user_janela_login():
            self.nome_procurado = self.login.nome_get()
            self.senha_procurado = self.login.senha_get()
            self.carrega_user = CarregarUsuario(self.nome_procurado, self.senha_procurado)
            
            # Verifique se o usuário não foi encontrado
            if not self.carrega_user.resposta:
                return
            
            # Se necessário, mostre uma mensagem e abra a janela de registro
            self.abrir_janela_registro()

        self.root.destroy()
        self.window = tk.Tk()
        self.login = Login(self.window)
        self.login.button_login.config(command=check_user_janela_login)

    def config_check(self):
        self.mostre_senha = tk.IntVar()
        self.registro.mostrar_senha.config(variable=self.mostre_senha, command=self.ocultar_senha)

    def config_button_enviar(self):
        self.registro.button_enviar.config(command=self.salvar_usuario)

    def ocultar_senha(self):
        if self.mostre_senha.get() == 1:
            self.registro.senha_entrada.config(show='')
            self.registro.mostrar_senha.config(text='Ocultar senha')
        else:
            self.registro.senha_entrada.config(show='*')
            self.registro.mostrar_senha.config(text='Mostrar senha')

    def config_eventos(self):
        self.registro.nome_entrada.bind('<KeyRelease>', self.dicas_nome)
        self.registro.senha_entrada.bind('<KeyRelease>', self.dicas_senha)
        self.registro.data_entrada.bind('<KeyRelease>', self.dicas_data)

    def dicas_nome(self, event):
        nome = self.registro.nome_get()
        ler_nome = len(nome)

        if 5 <= ler_nome <= 9:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário está no número de caracteres mínimo, pois tem {ler_nome}!', fg='green', wraplength=200)
        elif ler_nome == 10:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário chegou ao número de caractere máximo, pois tem {ler_nome}!', fg='green', wraplength=200)
        elif ler_nome >= 11:
            Mensagens.msgAtencao(f'Seu nome de usuário chegou ao número de caractere máximo, pois tem {ler_nome}!')
            self.registro.nome_entrada.delete(1.0, tk.END)
            self.registro.nome_dicas.config(text='Entrada resetada')
        else:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário não chegou ao número de caractere mínimo, pois tem {ler_nome}!', fg='red', wraplength=200)
            if ler_nome <= 1:
                self.registro.nome_dicas.config(text=f'Seu nome de usuário é insuficiente, pois tem {ler_nome} caractere!', fg='red', wraplength=200)

    def dicas_senha(self, event):
        senha = self.registro.senha_get()
        ler_senha = len(senha)

        if 5 <= ler_senha <= 9:
            self.registro.senha_dicas.config(text=f'Sua senha de usuário está no número de caracteres mínimo, pois tem {ler_senha}!', fg='green', wraplength=200)
        elif ler_senha == 10:
            self.registro.senha_dicas.config(text=f'Sua senha de usuário chegou ao número de caractere máximo, pois tem {ler_senha}!', fg='green', wraplength=200)
        elif ler_senha >= 11:
            Mensagens.msgAtencao(f'Sua senha de usuário chegou ao número de caractere máximo, pois tem {ler_senha}!')
            self.registro.senha_entrada.delete(0, tk.END)
            self.registro.senha_dicas.config(text='Entrada resetada')
        else:
            self.registro.senha_dicas.config(text=f'Sua senha de usuário não chegou ao número de caractere mínimo, pois tem {ler_senha}!', fg='red', wraplength=200)
            if ler_senha <= 1:
                self.registro.senha_dicas.config(text=f'Sua senha de usuário é insuficiente, pois tem {ler_senha} caractere!', fg='red', wraplength=200)

    def dicas_data(self, event):
        try:
            data_formatada = datetime.strptime(self.registro.data_get(), '%d-%m-%Y')
            data_padrao = data_formatada.strftime('%d-%m-%Y')
            self.registro.data_dicas.config(text=f'Sua data de nascimento ficou: {data_padrao}', fg='green')
        except ValueError:
            self.registro.data_dicas.config(text='Inválido', fg='red')

    def salvar_usuario(self):
        nome = self.registro.nome_get()
        senha = self.registro.senha_get()
        data = self.registro.data_get()

        def verificar_campo_vazio():
            nome_status = self.registro.nome_dicas
            senha_status = self.registro.senha_dicas
            data_status = self.registro.data_dicas

            if nome == '' and senha == '' and data == '':
                Mensagens.msgAtencao('Os três campos estão vazios, preencha por favor!')
            elif nome_status.cget('fg') == 'red' and senha_status.cget('fg') == 'red' and data_status.cget('fg') == 'red':
                Mensagens.msgAtencao('Os três campos não seguem os requisitos! Preencha por favor!')
            elif nome_status.cget('fg') == 'red' and senha_status.cget('fg') == 'red':
                Mensagens.msgAtencao('Os campos nome e senha não seguem os requisitos! Preencha por favor!')
            elif nome_status.cget('fg') == 'red' and data_status.cget('fg') == 'red':
                Mensagens.msgAtencao('Os campos nome e data não seguem os requisitos! Preencha por favor!')
            elif senha_status.cget('fg') == 'red':
                Mensagens.msgAtencao('O campo senha não segue requisitos! Preencha por favor!')
            elif nome_status.cget('fg') == 'red':
                Mensagens.msgAtencao('O campo nome não segue requisitos! Preencha por favor!')
            elif data_status.cget('fg') == 'red':
                Mensagens.msgAtencao('O campo data não segue requisitos! Preencha por favor!')
            elif nome == '':
                Mensagens.msgAtencao('O campo nome está vazio, preencha por favor!')
            elif senha == '':
                Mensagens.msgAtencao('O campo senha está vazio, preencha por favor!')
            elif data == '':
                Mensagens.msgAtencao('O campo data está vazio, preencha por favor!')
            else:
                self.contar_click += 1
                if self.contar_click >= 2:
                    Mensagens.msgAtencao('Seu cadastro já foi enviado!')
                else:
                    self.registro.nome_entrada.config(state=tk.DISABLED)
                    self.registro.data_entrada.config(state=tk.DISABLED)
                    self.registro.senha_entrada.config(state=tk.DISABLED)
                    SalvarUsuario(nome, datetime.strptime(data, '%d-%m-%Y'), senha)
                    self.abrir_janela_login()
        
        verificar_campo_vazio()

# Código principal para iniciar a aplicação
app = tk.Tk()
control = Controle(app)
app.mainloop()
