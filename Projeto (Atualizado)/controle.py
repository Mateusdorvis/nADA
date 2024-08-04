import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Textcustomizado
from sistema_login import Registro
from modelo import SalvarUsuario, CarregarUsuario
from datetime import datetime

class Controle:
    def __init__(self, root):
        self.root = root
        self.registro = Registro(root)

        self.registro.button_enviar.config(command=self.salvar_usuario)

        self.registro.nome_entrada.bind('<KeyRelease>',self.dicas_nome)

        self.registro.senha_entrada.bind('<KeyRelease>',self.dicas_senha)

        self.registro.data_entrada.bind('<KeyRelease>',self.dicas_data)
        
    def dicas_nome(self, event):
        
        self.ler_nome = len(self.registro.nome_get())
        self.nome_status = self.registro.nome_dicas
        if self.ler_nome>=5 and self.ler_nome<=9:
            self.nome_status.config(text=f'Seu nome de usuário está no números de caracteres mínimo, pois tem {self.ler_nome} !',fg='green', wraplength=200)
            
        elif self.ler_nome==10:
            self.nome_status.config(text=f'Seu nome de usuário chegou ao número de caractere máximo, pois tem {self.ler_nome} !',fg='green', wraplength=200)
        
        elif self.ler_nome>=11:
            self.nome_status.config(text=f'Seu nome de usuário chegou número de caractere máximo, pois tem {self.ler_nome} !',fg='red', wraplength=200)
        
        else:
            self.nome_status.config(text=f'Seu nome de usuário não chegou ao  número de caractere mínimo, pois tem {self.ler_nome} !',fg='red', wraplength=200)
            if self.ler_nome<=1:
                self.nome_status.config(text=f'Seu nome de usuário é insuficente, pois tem {self.ler_nome}  caractere !',fg='red', wraplength=200)
        
    def dicas_senha(self, event):
            self.ler_senha = len(self.registro.senha_get())
            self.senha_status = self.registro.senha_dicas
            if self.ler_senha>=5 and self.ler_senha<=9:
                self.nome_status.config(text=f'Sua senha de usuário está no números de caracteres mínimo, pois tem {self.ler_senha} !',fg='green', wraplength=200)
                
            elif self.ler_senha==10:
                self.nome_status.config(text=f'Sua senha de usuário chegou ao número de caractere máximo, pois tem {self.ler_senha} !',fg='green', wraplength=200)
            
            elif self.ler_senha>=11:
                self.nome_status.config(text=f'Sua senha de usuário chegou número de caractere máximo, pois tem {self.ler_senha} !',fg='red', wraplength=200)
            
            else:
                self.senha_status.config(text=f'Sua senha de usuário não chegou ao  número de caractere mínimo, pois tem {self.ler_senha} !',fg='red', wraplength=200)
                if self.ler_senha<=1:
                    self.nome_status.config(text=f'Sua senha de usuário é insuficente, pois tem {self.ler_senha}  caractere !',fg='red', wraplength=200)

    def dicas_data(self, event):
        try:
            self.data_formatada = datetime.strptime(self.registro.data_get(), '%d-%m-%Y')
            self.data_padrao =  self.data_formatada.strftime('%d-%m-%Y')
            self.registro.data_dicas.config(text=f'Sua  data de nascimento ficou : {self.data_padrao}', fg='green')

        except ValueError:
            self.registro.data_dicas.config(text='Inválido', fg='red')




            



    
    def salvar_usuario(self):
        self.nome = self.registro.nome_get()
        self.senha = self.registro.senha_get()
        self.data = self.registro.data_get()

        if self.nome == '' and self.senha == '' and self.data == '':
            Mensagens.msgAtencao('Os três campos estão vazios, preencha por favor!')
        
        elif self.nome != '' and self.senha == '' and self.data == '':
            Mensagens.msgAtencao('Os  campos data e senha estão vazios, preencha por favor!')
        
        elif self.nome == '' and self.senha != '' and self.data == '':
            Mensagens.msgAtencao('Os campos data e nome estão vazios, preencha por favor!')
        
        elif self.nome == '' and self.senha == '' and self.data != '':
            Mensagens.msgAtencao('Os  campos nome e senha estão vazios, preencha por favor!')

        elif self.nome == '':
            Mensagens.msgAtencao('O campo nome está vazio, preencha por favor!')
        elif self.senha == '':
            Mensagens.msgAtencao('O campo senha está vazio, preencha por favor!')
        elif self.data == '':
            Mensagens.msgAtencao('O campo data está vazio, preencha por favor!')
        else:
            Mensagens.msgInfo('Seu cadastro foi realizado com sucesso !')


        



root = tk.Tk()
x = Controle(root)
root.mainloop()
    
        
        