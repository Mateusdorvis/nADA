import tkinter as tk
from tkinter import ttk
from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Buttoncustomizado
from cadastro import Cadastro

class Login(Cadastro):
    def __init__(self, root):
        super().__init__(root)
        self.root.title('Login de usuário')
    #desabilitand o campo data
    def entrada_data(self):
        pass

    def eventoTeclado_Data(self, event):
        pass

    def data_get(self):
        pass
    
    def enviarCadastro(self):

        if self.nome_get()=='' and self.senha_get()=='':
            Mensagens.msgAtencao('Preencha os dois campos !')
            
        elif self.nome_get()!='' and self.senha_get()=='':
            Mensagens.msgAtencao('Preencha o campo senha !')
        
        elif self.nome_get()=='' and self.senha_get()!='':
            Mensagens.msgAtencao('Preencha o campo nome !')

        elif self.nome_status.cget('fg')=='red' and self.senha_status.cget('fg')=='red':  
            Mensagens.msgAtencao('Todos os campos foram inseridos de maneira inadequada  !')

        elif self.nome_status.cget('fg')!='red'  and self.senha_status.cget('fg')=='red':  
            Mensagens.msgAtencao('O campo SENHA , não foi preenchido adequadamente  !') 

        elif self.nome_status.cget('fg')=='red' and self.senha_status.cget('fg')!='red':  
            Mensagens.msgAtencao('O campo NOME, não foi preenchido de forma adequada!') 

        else:
            self.contar+=1
            if self.contar>=2:
                Mensagens.msgAtencao('Seu cadastro já foi enviado !')
            else:
                    Mensagens.msgInfo(f'Seu login {self.nome_get()}, foi realizado com sucesso !')
                    self.nome_text_entry.config(state=tk.DISABLED)
                    self.senha_text_entry.config(state=tk.DISABLED)
                    



        