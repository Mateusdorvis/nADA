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
        self.config_eventos()

    
    def config_eventos(self):
        self.registro.nome_entrada.bind('<KeyRelease>', self.dicas_nome)
        self.registro.senha_entrada.bind('<KeyRelease>', self.dicas_senha)
        self.registro.data_entrada.bind('<KeyRelease>', self.dicas_data)
       
    def dicas_nome(self, event):
        
        self.ler_nome = len(self.registro.nome_get())

        if self.ler_nome>=5 and self.ler_nome<=9:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário está no números de caracteres mínimo, pois tem {self.ler_nome} !',fg='green', wraplength=200)
            
        elif self.ler_nome==10:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário chegou ao número de caractere máximo, pois tem {self.ler_nome} !',fg='green', wraplength=200)
        
        elif self.ler_nome>=11:
            Mensagens.msgAtencao(f'Seu nome de usuário chegou número de caractere máximo, pois tem {self.ler_nome} !')
            self.registro.nome_entrada.delete(1.0, tk.END)
        
        else:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário não chegou ao  número de caractere mínimo, pois tem {self.ler_nome} !',fg='red', wraplength=200)
            if self.ler_nome<=1:
                self.registro.nome_dicas.config(text=f'Seu nome de usuário é insuficente, pois tem {self.ler_nome}  caractere !',fg='red', wraplength=200)
        
    def dicas_senha(self, event):
            self.ler_senha = len(self.registro.senha_get())

            if self.ler_senha>=5 and self.ler_senha<=9:
                self.registro.senha_dicas.config(text=f'Sua senha de usuário está no números de caracteres mínimo, pois tem {self.ler_senha} !',fg='green', wraplength=200)
                
            elif self.ler_senha==10:
                self.registro.senha_dicas.config(text=f'Sua senha de usuário chegou ao número de caractere máximo, pois tem {self.ler_senha} !',fg='green', wraplength=200)
            
            elif self.ler_senha>=11:
                Mensagens.msgAtencao(f'Sua senha de usuário chegou número de caractere máximo, pois tem {self.ler_senha} !')
                self.registro.senha_entrada.delete(0, tk.END)
                self.registro.senha_dicas.config(text='Entrada resetada')
            
            else:
                self.registro.senha_dicas.config(text=f'Sua senha de usuário não chegou ao  número de caractere mínimo, pois tem {self.ler_senha} !',fg='red', wraplength=200)
                if self.ler_senha<=1:
                    self.registro.senha_dicas.config(text=f'Sua senha de usuário é insuficente, pois tem {self.ler_senha}  caractere !',fg='red', wraplength=200)

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

        def verificar_campo_vazio():
            nome_status = self.registro.nome_dicas
            senha_status = self.registro.senha_dicas
            data_status = self.registro.data_dicas

            
            if self.nome == '' and self.senha == '' and self.data == '':
                Mensagens.msgAtencao('Os três campos estão vazios, preencha por favor!')
            

            elif nome_status.cget('fg')=='red' and data_status.cget('fg')=='red' and senha_status.cget('fg')=='red':
                Mensagens.msgAtencao('Os três campos não seguem os requisitos ! Preencha por favor!')

            elif nome_status.cget('fg')!='red' and data_status.cget('fg')=='red' and senha_status.cget('fg')=='red':
                Mensagens.msgAtencao('Os campos data  e senha   não seguem os requisitos ! Preencha por favor!')
            
            elif nome_status.cget('fg')=='red' and data_status.cget('fg')!='red' and senha_status.cget('fg')=='red':
                Mensagens.msgAtencao('Os campos nome  e senha  não seguem os requisitos ! Preencha por favor!')
            
            elif nome_status.cget('fg')=='red' and data_status.cget('fg')=='red' and senha_status.cget('fg')!='red':
                Mensagens.msgAtencao('Os campos nome  e data  não seguem os requisitos ! Preencha por favor!')
            
            elif senha_status.cget('fg')=='red':
                Mensagens.msgAtencao('O campo senha não segue requisitos ! Preencha por favor!')
            
            elif nome_status.cget('fg')=='red':
                Mensagens.msgAtencao('O campo nome não segue requisitos ! Preencha por favor!')
            
            elif data_status.cget('fg')=='red':
                Mensagens.msgAtencao('O campo data não segue requisitos ! Preencha por favor!')
            
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
            
            elif  nome_status.cget('fg')=='red' and self.data == '' and self.senha == '' :
                Mensagens.msgAtencao('O campo nome não seguiu os requsitos e ademais, os campos data e senha estão vazios, preencha por favor!')
            else:
                Mensagens.msgInfo('Seu cadastro foi realizado com sucesso !')
            
        verificar_campo_vazio()

     

        



root = tk.Tk()
x = Controle(root)
root_m = tk.Tk()
login = Login(root_m)
root.mainloop()
root_m.mainloop()
    
        
        