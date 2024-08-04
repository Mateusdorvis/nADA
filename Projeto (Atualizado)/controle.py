import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Textcustomizado
from sistema_login import Registro
from modelo import SalvarUsuario, CarregarUsuario

class Controle:
    def __init__(self, root):
        self.root = root
        self.registro = Registro(root)
     
        self.registro.button_enviar.config(command=self.salvar_usuario)
        
    def evento_tecla
    
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
            Mensagens.msgSucesso('Seu cadastro foi realizado com sucesso !')


        



root = tk.Tk()
x = Controle(root)
root.mainloop()
    
        
        