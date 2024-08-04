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

        self.cadastro.nome_text_entry.bind('<KeyRelease>', self.EventoCampoNome)

        self.cadastro.senha_text_entry.bind('<KeyRelease>', self.EventoCampoSenha)


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
        elif self.cadastro.data_get():
            try:
                    data_formatada = datetime.strptime(self.cadastro.data_get(), '%d-%m-%Y')
                    data_padrao = data_formatada.strftime('%d-%m-%Y')
                  
                
            except ValueError:
                    Mensagens.msgAtencao('Insira uma data de nascimento no formato dd-mm-YYYY !')
                      
            
        else:
            self.cadastro.contar+=1
            if self.cadastro.contar>=2:
                Mensagens.msgAtencao('Seu cadastro já foi enviado !')
            else:
                Mensagens.msgInfo(f'Sua data de nascimento ficou {data_padrao}')
                Mensagens.msgInfo('Cadastro Realizado com sucesso !')
                save_user = SalvarUsuario(self.cadastro.nome_get(),data_formatada,self.cadastro.senha_get())
                


    def ler_campo_senha(self):
        return len(self.cadastro.senha_get())
    
    def ler_campo_nome(self):
        return len(self.cadastro.nome_get())
    

    def EventoCampoSenha(self, event):
        if self.ler_campo_senha()>=5 and self.ler_campo_senha()<=9:
            self.cadastro.senha_status.config(text=f'Sua senha atingiu número de caracteres mínimo, pois tem {self.ler_campo_senha()} !', fg='green')

        elif self.ler_campo_senha()==10:
            self.cadastro.senha_status.config(text=f'Sua senha atingiu número de caracteres máximo, pois tem {self.ler_campo_senha()} !', fg='gren')

        elif self.ler_campo_senha()>=11:
            self.cadastro.senha_status.config(text=f'Sua senha passou do número de caracteres máximo, pois tem {self.ler_campo_senha()} !', fg='red')
            self.cadastro.senha_text_entry.delete(1.0, tk.END)
        
        else:
            self.cadastro.senha_status.config(text=f'Escreva mais, porque sua senha  tem  apenas {self.ler_campo_senha() } caracteres !', fg='red')
            if self.ler_campo_senha()<=1:
                self.cadastro.senha_status.config(text=f'Senha insuficente, pois tem {self.ler_campo_senha()} caractere !', fg='red')


    def EventoCampoNome(self, event):
        if self.ler_campo_nome()>=5 and self.ler_campo_nome()<=9:
            self.cadastro.nome_status.config(text=f'Seu nome atingiu número de caracteres mínimo, pois tem {self.ler_campo_nome()} !', fg='green')

        elif self.ler_campo_nome()==10:
            self.cadastro.nome_status.config(text=f'Seu nome atingiu número de caracteres máximo, pois tem {self.ler_campo_nome()} !', fg='green')
        
        elif self.ler_campo_nome()>=11:
            self.cadastro.nome_status.config(text=f'Seu nome de usuário passou do número de caracteres máximo, pois tem {self.ler_campo_nome()} !', fg='red')
            self.cadastro.nome_text_entry.delete(1.0, tk.END)
        
        else:
            self.cadastro.nome_status.config(text=f'Escreva mais, porque seu nome  tem  apenas {self.ler_campo_nome() } caracteres !', fg='red')

            if self.ler_campo_nome()<=1:
                self.cadastro.nome_status.config(text=f'Nome de usuário insuficente, pois tem {self.ler_campo_nome()} caractere !', fg='red')



       


if __name__=='__main__':
    root= tk.Tk()
    app = Controle(root)
    root.mainloop()
        

