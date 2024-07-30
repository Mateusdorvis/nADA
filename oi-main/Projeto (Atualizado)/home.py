import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as ft
from login_v import NovoLogin, Login
from elementos import MensagensProntas


class PaginaInicial:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Aplicativo de baixar roms de jogos')
        self.menu_barra = tk.Menu(self.root)
       
        self.root.config(menu=self.menu_barra)
        self.root.config(bg='white')
        self.iniciar_menu_opcao()
        self.iniciar_menu_login()
        self.mostar_status_conta()
        self.root.mainloop()
    

    def mostar_status_conta(self):
         self.menu_barra.add_command(label='Status da conta  do usuário : DESATIVADO ')
         self.menu_barra.entryconfig('Status da conta  do usuário : DESATIVADO ', state=tk.DISABLED)

    def iniciar_menu_opcao(self):
        def Backgrounds(cor):
                self.root.config(bg=cor)

        def Sair():
            resposta = MensagensProntas.messageSimNao('Tem certeza que deseja sair do app ?')
            if resposta:
                self.root.quit()

        self.menu_config = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_config.add_command(label='Sair do app', command=Sair)
        self.menu_barra.add_cascade(label='Configurações do app', menu=self.menu_config)
            
        def submenu_opc_AlterarCor(): 
                lista_cores_disponiveis = [
                        {'label': 'Amarelo','command': lambda : Backgrounds ('#F0D911')},
                        {'label': 'Azul','command': lambda : Backgrounds ('#1359F0')},
                        {'label': 'Laranja','command':  lambda :Backgrounds ('#F08A1D')},
                        {'label': 'Normal','command':  lambda : Backgrounds ('white')},
                        {'label': 'Preto','command': lambda : Backgrounds ('black')},
                        {'label': 'Rosa','command':  lambda : Backgrounds ('#F069B8')},
                        {'label': 'Verde','command':  lambda : Backgrounds ('#ADF032')},
                        {'label': 'Vermelho','command': lambda :  Backgrounds ('#F02214')}
                        ]
                corfundo = tk.Menu(self.menu_config, tearoff=0)
                for cada_item_lista in lista_cores_disponiveis:
                        corfundo.add_command(label= cada_item_lista['label'], command= cada_item_lista['command'])

                self.menu_config.add_cascade(label='Alterar cor de fundo para...', menu=corfundo)
        submenu_opc_AlterarCor()

    def iniciar_menu_login(self):
        def abrir_cadastro():
            self.root.withdraw()
            self.menu_barra.entryconfig('Login', state=tk.DISABLED)
           #função que serve para confirmar que o usuário está cadastrado
            def Confirmar_cadastrado(nome, data, senha):
                messagebox.showinfo('Boas vindas', f' Olá {nome} !')
                self.menu_barra.entryconfig('Login', state=tk.DISABLED)
                self.root.deiconify()
                #atualiza 
                self.menu_barra.delete('Status da conta  do usuário : DESATIVADO ')
                #para isso
                self.menu_barra.add_command(label='Status da conta  do usuário : ATIVADO ')
                
                status = tk.Menu(self.menu_barra, tearoff=0)
                status.add_command(label=f'Senha do usuário {nome} : {senha}')
                status.add_command(label=f'Data de nascimento do usuário {nome} : {data}')
                self.menu_barra.add_cascade(label=f'Usuario : {nome}', menu=status)

            cadastro = NovoLogin(Confirmar_cadastrado)

        def fazer_login():
            self.menu_barra.entryconfig('Login', state=tk.DISABLED)
            self.root.withdraw()
            def Confirmar_login(nome, senha, data):
                self.root.deiconify()
                messagebox.showinfo('Boas vindas', f' Olá {nome} !')
                self.menu_barra.entryconfig('Login', state=tk.DISABLED)
                #atualiza 
                self.menu_barra.delete('Status da conta  do usuário : DESATIVADO ')
                #para isso
                self.menu_barra.add_command(label='Status da conta  do usuário : ATIVADO ')
                
                status = tk.Menu(self.menu_barra, tearoff=0)
                status.add_command(label=f'Data de nascimento do usuário {nome} : {data}')
                status.add_command(label=f'Senha do usuário {nome} : {senha}')
                self.menu_barra.add_cascade(label=f'Usuario : {nome}', menu=status)
            cadastro = Login(Confirmar_login)

            
        self.menu_login = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_login.add_command(label='Realizar novo cadastro', command = abrir_cadastro)
        self.menu_login.add_command(label='Entrar', command =  fazer_login )
        self.menu_barra.add_cascade(label='Login', menu=self.menu_login)
        
    
if __name__=='__main__':
   PaginaInicial()

           
