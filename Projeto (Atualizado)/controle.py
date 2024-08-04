import tkinter as tk

from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens
from cadastro import Cadastro
from Salvadados import SalvarUsuario
from datetime import datetime


class Controle:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro(self.root)
        self.button_enviar = Buttoncustomizado(self.cadastro.box_frame, text='Enviar cadastro', command=self.enviarCadastro)
        self.button_enviar.grid(row=15, column=0, sticky=tk.NSEW)
    
    def enviarCadastro(self):
        if self.cadastro.nome_get()=='' and self.cadastro.senha_get()=='' and self.cadastro.data_get()=='':
            Mensagens.msgAtencao('Preencha os três campos por favor !')

        elif self.cadastro.nome_get()!='' and self.cadastro.senha_get()=='' and self.cadastro.data_get()=='':
            Mensagens.msgAtencao('Preencha os campos DATA e SENHA por favor !')

        elif self.cadastro.nome_get()=='' and self.cadastro.senha_get()!='' and self.cadastro.data_get()=='':
            Mensagens.msgAtencao('Preencha os campos DATA e NOME por favor !')

        elif self.cadastro.nome_get()=='' and self.cadastro.senha_get()=='' and self.cadastro.data_get()!='':
            Mensagens.msgAtencao('Preencha os campos NOME e SENHA por favor !')
        
        elif self.cadastro.nome_get()=='':
            Mensagens.msgAtencao('Preencha o campo NOME  por favor !')
        
        elif self.cadastro.senha_get()=='':
            Mensagens.msgAtencao('Preencha o campo SENHA  por favor !')
        
        elif self.cadastro.data_get()=='':
            Mensagens.msgAtencao('Preencha o campo DATA  por favor !')
        
        def EventoCampoNome(self):
            



       


if __name__=='__main__':
    root= tk.Tk()
    app = Controle(root)
    root.mainloop()
        

