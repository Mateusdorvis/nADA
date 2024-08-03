import tkinter as tk

from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens
from login import Login
from cadastro import Cadastro
from Salvadados import SalvarUsuario
from datetime import datetime


class Controle:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro(self.root)
        self.button_enviar = Buttoncustomizado(self.cadastro.box_frame, text='Enviar cadastro', width=20, command=self.salvar_usuario)
        
    

    def salvar_usuario(self):
        
        if self.cadastro.nome_get()=='' and self.cadastro.senha_get()=='' and self.cadastro.data_get()=='':
            Mensagens.msgAtencao('Preencha os três campos !')
            
        elif self.cadastro.nome_get()!='' and self.senha_get()=='' and self.cadastro.data_get()=='':
            Mensagens.msgAtencao('Preencha o campo senha e data !')
        
        elif self.cadastro.nome_get()=='' and self.cadastro.senha_get()!='' and self.cadastro.data_get()=='':
            Mensagens.msgAtencao('Preencha o campo nome e data !')
        
        elif self.cadastro.nome_get()=='' and self.cadastro.senha_get()=='' and self.cadastro.data_get()!='':
            Mensagens.msgAtencao('Preencha o campo nome e senha !')
            
        
        elif self.cadastro.senha_get()=='':
            Mensagens.msgAtencao('Preencha o campo senha !')
        
        elif self.cadastro.nome_get()=='':
            Mensagens.msgAtencao('Preencha o campo nome !')
            
        elif self.cadastro.data_get()=='':
            Mensagens.msgAtencao('Preencha o campo  data !')

        elif self.cadastro.nome_status.cget('fg')=='red' and self.cadastro.data_status.cget('fg')=='red' and self.senha_status.cget('fg')=='red':  
            Mensagens.msgAtencao('Todos os campos foram inseridos de maneira inadequadamente  !')

        elif self.cadastro.nome_status.cget('fg')!='red' and self.cadastro.data_status.cget('fg')=='red' and self.cadastro.senha_status.cget('fg')=='red':  
            Mensagens.msgAtencao('Os campos SENHA e DATA, não foram preenchidos de forma adequada  !') 

        elif self.cadastro.nome_status.cget('fg')=='red' and self.cadastro.data_status.cget('fg')!='red' and self.cadastro.senha_status.cget('fg')=='red':  
            Mensagens.msgAtencao('Os campos NOME e SENHA, não foram preenchidos de forma adequada!') 

        elif self.cadastro.nome_status.cget('fg')=='red' and self.cadastro.data_status.cget('fg')=='red' and self.cadastro.senha_status.cget('fg')!='red':  
            Mensagens.msgAtencao('Os campos NOME e DATA, não foram preenchidos de forma adequada!') 

        elif self.cadastro.nome_status.cget('fg')=='red':  
            Mensagens.msgAtencao('O campo NOME  não segue os requistos  desejados !')

        elif self.cadastro.data_status.cget('fg')=='red':  
            Mensagens.msgAtencao(f'O campo DATA {self.nome_get()}, NÃO segue os requistos desejados  !')  

        elif self.cadastro.senha_status.cget('fg')=='red':  
            Mensagens.msgAtencao(f'O campo SENHA {self.nome_get()}, NÃO  segue os requistos  desejados !')        
        
            
         
            
        else:
            self.cadastro.contar+=1
            if self.cadastro.contar>=2:
                Mensagens.msgAtencao('Seu cadastro já foi enviado !')
            else:
                    Mensagens.msgInfo(f'Seu cadastro {self.cadastro.nome_get()}, foi realizado com sucesso !')
                    self.cadastro.nome_text_entry.config(state=tk.DISABLED)
                    self.cadastro.data_text_entry.config(state=tk.DISABLED)
                    self.cadastro.senha_text_entry.config(state=tk.DISABLED)
                    
            
        
        
            
    
        
        self.button_enviar.grid(row=13, column=0, pady=5, padx=10)
        nome_cadastrado = self.cadastro.nome_get()
        data_cadastrada = self.cadastro.formata_data()
        senha_cadastrada = self.cadastro.senha_get()
        data = datetime.strptime(data_cadastrada, '%Y-5m-%d')


        save_users = SalvarUsuario(nome_cadastrado, data, senha_cadastrada)
        print(save_users)


if __name__=='__main__':
    root= tk.Tk()
    app = Controle(root)
    root.mainloop()
        

