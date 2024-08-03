import tkinter as tk
from datetime import datetime
from tkinter import Widget, ttk
from tkinter import messagebox
from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens



class Cadastro:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x400') 
        
        self.root.title('Cadastro de usuário')
        self.root.config(bg='#2f6f8e')
        self.entrada_nome()
        self.contar = 0
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        self.button_enviar = Buttoncustomizado(self.box_frame, text='Enviar cadastro', width=20, command=self.enviarCadastro)
        self.button_enviar.grid(row=13, column=0, pady=5)
        
        self.entrada_data()
        self.entrada_senha()
        self.root.mainloop()
    
  
        
    def enviarCadastro(self):
        
        
        if self.nome_get()=='' and self.senha_get()=='' and self.data_get()=='':
            Mensagens.msgAtencao('Preencha os três campos !')
            
        elif self.nome_get()!='' and self.senha_get()=='' and self.data_get()=='':
            Mensagens.msgAtencao('Preencha o campo senha e data !')
        
        elif self.nome_get()=='' and self.senha_get()!='' and self.data_get()=='':
            Mensagens.msgAtencao('Preencha o campo nome e data !')
        
        elif self.nome_get()=='' and self.senha_get()=='' and self.data_get()!='':
            Mensagens.msgAtencao('Preencha o campo nome e senha !')
            
        
        elif self.senha_get()=='':
            Mensagens.msgAtencao('Preencha o campo senha !')
        
        elif self.nome_get()=='':
            Mensagens.msgAtencao('Preencha o campo nome !')
            
        elif self.data_get()=='':
            Mensagens.msgAtencao('Preencha o campo  data !')
            
        
            
         
            
        else:
            self.contar+=1
            if self.contar>=2:
                Mensagens.msgAtencao('Seu cadastro já foi enviado !')
            else:
                    Mensagens.msgInfo(f'Seu cadastro {self.nome_get()}, foi realizado com sucesso !')
                    self.nome_text_entry.config(state=tk.DISABLED)
                    self.data_text_entry.config(state=tk.DISABLED)
                    self.senha_text_entry.config(state=tk.DISABLED)
                    
            
        
        
            
    
   
    def nome_get(self):
            return self.nome_text_entry.get(1.0, tk.END).strip()
            
    def data_get(self):
            return self.data_text_entry.get(1.0, tk.END).strip()
            
    def senha_get(self):
            return self.senha_text_entry.get(1.0, tk.END).strip()
        
    def entrada_nome(self):
        
        self.box_frame = tk.Frame(self.root, width=400, height=400, bg='white', borderwidth=0, relief=None)
        
        self.box_frame.grid(row=0, column=0)
       

        self.nome_titulo = LabelcustomizadaTitulo(self.box_frame, text='CAMPO NOME')
        self.nome_titulo.grid(row=0, column=0, sticky=tk.NSEW)

        self.nome_label = Labelcustomizada(self.box_frame,
                                                text='Digite seu nome :')
        self.nome_label.grid(row=1, column=0, padx=5, pady=5)

        self.nome_text_entry = tk.Text(self.box_frame, width=12, height=0)
        self.nome_text_entry.grid(row=1, column=1, padx=5, pady=5)

        self.nome_status = Labelcustomizada(self.box_frame)
        self.nome_status.grid(row=3, column=0, sticky=tk.NSEW)

        self.nome_text_entry.bind('<KeyRelease>', self.eventoTeclado_Nome)

    def entrada_data(self):
        self.data_titulo = LabelcustomizadaTitulo(self.box_frame,
                                    text='CAMPO DATA.')
        self.data_titulo.grid(row=5, column=0, sticky=tk.NSEW)

        self.data_label = Labelcustomizada(self.box_frame, text='Digite sua data de nascimento (ex. 23-09-2020) :')
        self.data_label.grid(row=6, column=0, sticky=tk.NSEW)

        self.data_text_entry = tk.Text(self.box_frame, width=12, height=0)
        self.data_text_entry.grid(row=6, column=1, sticky=tk.NSEW)

        self.data_status = Labelcustomizada(self.box_frame, wraplength=200)
        self.data_status.grid(row=7, column=1, sticky=tk.NSEW)
        self.data_text_entry.bind('<KeyRelease>', self.eventoTeclado_Data)
        

    def entrada_senha(self):
        self.senha_titulo = LabelcustomizadaTitulo(self.box_frame,
                                     text='CAMPO SENHA.')
        self.senha_titulo.grid(row=9, column=0, sticky=tk.NSEW)

        self.senha_label = Labelcustomizada(self.box_frame,
                                                 text='Digite sua senha :')
        self.senha_label.grid(row=10, column=0, sticky=tk.NSEW)

        self.senha_text_entry = tk.Text(self.box_frame, width=12, height=0)
        self.senha_text_entry.grid(row=10, column=1, sticky=tk.NSEW)

        self.senha_status = Labelcustomizada(self.box_frame, wraplength=200)
        self.senha_status.grid(row=11, column=0, sticky=tk.NSEW)

        self.senha_text_entry.bind('<KeyRelease>', self.eventoTeclado_Senha)

    #nome eventos
    def eventoTeclado_Nome(self, event):
        pegue_nome = self.nome_get()
        ler_caractere_nome = len(pegue_nome)
        if ler_caractere_nome >= 5 and ler_caractere_nome <= 10:
            self.nome_status.config(
                text=f'Tem {ler_caractere_nome} caracteres !', fg='green')

        elif ler_caractere_nome >= 11:
            self.nome_text_entry.config(state=tk.DISABLED)
            Mensagens.msgAtencao(
                f'Você atingiu número máximo de caracteres, pois tem {ler_caractere_nome} ! Por isso resertando o campo nome'
            )
            self.nome_text_entry.config(state=tk.NORMAL)
            self.nome_text_entry.delete(1.0, tk.END)
            self.nome_status.config(text='Entrada resetada', fg='green')

        else:
            self.nome_status.config(
                text=f'Tem {ler_caractere_nome} caracteres !', fg='red')
            if ler_caractere_nome <= 1:
                self.nome_status.config(
                    text=f'Tem {ler_caractere_nome} caractere !', fg='red')
                self.root.after(
                    30000, lambda: self.nome_status.config(
                        text='Não se esqueça de preencher este campo !'))

    #senha
    def eventoTeclado_Senha(self, event):
        pegue_senha = self.senha_get()
        ler_caractere_senha = len(pegue_senha)
        if ler_caractere_senha >= 5 and ler_caractere_senha <= 9:
            self.senha_status.config(
                text=
                f'A sua senha atingiu número mínimo de caracteres, porque tem {ler_caractere_senha} !',
                fg='green')

        elif ler_caractere_senha == 10:
            self.senha_status.config(
                text=
                f'A sua senha atingiu número máximo de caracteres, porque tem {ler_caractere_senha} !',
                fg='green')

        elif ler_caractere_senha >= 11:
            self.senha_text_entry.config(state=tk.DISABLED)
            Mensagens.msgAtencao(
                f'Sua senha passou do número máximo de caracteres, pois tem {ler_caractere_senha} ! Por isso resertando o campo senha...'
            )
            self.senha_text_entry.config(state=tk.NORMAL)
            self.senha_text_entry.delete(1.0, tk.END)
            self.senha_status.config(text='Entrada resetada', fg='green')

        else:
            self.senha_status.config(
                text=
                f'Sua senha tem somente {ler_caractere_senha} caracteres ? O mínimo é 5 e máximo é 10 !',
                fg='red')
            if ler_caractere_senha <= 1:
                self.senha_status.config(
                    text=
                    f'Digite uma senha que tenha de 5 a 10 caracteres ! Tem somente {ler_caractere_senha} caractere !',
                    fg='red')
                self.root.after(
                    300, lambda: self.senha_status.config(
                        text='Não se esqueça de preencher este campo !',
                        fg='green'))
                
    def eventoTeclado_Data(self, event):
        try:
                data_format = datetime.strptime(self.data_get(), '%d-%m-%Y')
                data_padrao = data_format.strftime('%d-%m-%Y')
                self.data_status.config(text=f' Sua data de nascimento ficou : {data_padrao}.', fg='green')
                
        
        except ValueError:
             self.data_status.config(text='Inválido', fg='red')
        
     

Cadastro()

        
        
        