import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Textcustomizado
from sistema_login import Registro
from modelo import SalvarUsuario, CarregarUsuario

class Controle:
    def __init__(self, root):
        self.root = root
        self.registro = Registro(root)

        self.registro.button_enviar.config(command=self.salvar_usuario)
        self.registro.nome_entrada.bind('<KeyRelease>',self.dicas_nome)
        
    def dicas_nome(self, event):
        
        self.ler_nome = len(self.registro.nome_get())
        self.nome_status = self.registro.nome_dicas
        if self.ler_nome>=5 and self.ler_nome<=9:
            self.nome_status.config(text=f'Seu nome de usuário está no números de caracteres mínimo, pois tem {self.ler_nome} !',fg='green', wraplength=50)
            
        elif self.ler_nome==10:
            self.nome_status.config(text=f'Seu nome de usuário chegou ao número de caractere máximo, pois tem {self.ler_nome} !',fg='green', wraplength=50)
        
        elif self.ler_nome>=11:
            self.nome_status.config(text=f'Seu nome de usuário chegou número de caractere máximo, pois tem {self.ler_nome} !',fg='red', wraplength=50)
        
        else:
            self.nome_status.config(text=f'Seu nome de usuário não chegou ao  número de caractere mínimo, pois tem {self.ler_nome} !',fg='red', wraplength=50)
            if self.ler_nome<=1:
                self.nome_status.config(text=f'Seu nome de usuário é insuficente, pois tem {self.ler_nome}  caractere !',fg='red', wraplength=50)


            



    
    def salvar_usuario(self):
        self.nome = self.registro.nome_get()
        self.senha = self.registro.senha_get()
        self.data = self.registro.data_get()
        if self.nome == '' and self.senha == '' and self.data == '':
            Mensagens.msgAtencao('Os três campos estão vazios, preencha por favor!')
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
    
        
        