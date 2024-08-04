import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Textcustomizado
from sistema_login import Registro, BaseCadastro, Login
from modelo import SalvarUsuario, CarregarUsuario
from datetime import datetime

class Controle:
    def __init__(self, root):
        self.root = root
        self.registro = Registro(root)
       
        self.registro.button_enviar.config(command=self.salvar_usuario)
    
    def salvar_usuario(self):
        self.nome = self.registro.nome_get()
        self.senha = self.registro.senha_get()
        self.data = self.registro.data_get()

        def verificar_campo_vazio():
            def verificar__cor():
                nome_status = self.registro.nome_dicas()
                senha_status = self.registro.nome_dicas()
                data_status = self.registro.nome_dicas()

                if nome_status
            
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
            verificar_campo_vazio()

     

        



root = tk.Tk()
x = Controle(root)
root_m = tk.Tk()
login = Login(root_m)
root.mainloop()
root_m.mainloop()
    
        
        