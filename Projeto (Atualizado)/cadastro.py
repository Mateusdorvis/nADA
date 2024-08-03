import tkinter as tk
from datetime import datetime
from tkinter import Label, Text
from tkinter import messagebox
from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens

class Cadastro:
    def __init__(self, root):
        self.root = root
        self.root.title('Cadastro de usuário')
        self.root.config(bg='#2f6f8e')
        self.entrada_nome()
        self.contar = 0
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        self.button_enviar = Buttoncustomizado(self.box_frame, text='Enviar cadastro', width=20, command=self.enviarCadastro)
        self.button_enviar.grid(row=13, column=0, pady=5, padx=10)
        
        self.entrada_data()
        self.entrada_senha()
    
    def enviarCadastro(self):
        if self.nome_get() == '' or self.data_get() == '' or self.senha_get() == '':
            Mensagens.msgAtencao('Preencha todos os campos!')
        else:
            self.contar += 1
            if self.contar >= 2:
                Mensagens.msgAtencao('Seu cadastro já foi enviado!')
            else:
                Mensagens.msgInfo(f'Seu cadastro {self.nome_get()} foi realizado com sucesso!')
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

        self.nome_label = Labelcustomizada(self.box_frame, text='Digite seu nome:')
        self.nome_label.grid(row=1, column=0, padx=5, pady=5)

        self.nome_text_entry = Text(self.box_frame, width=12, height=1)
        self.nome_text_entry.grid(row=1, column=1, padx=5, pady=5)

        self.nome_status = Labelcustomizada(self.box_frame)
        self.nome_status.grid(row=3, column=0, sticky=tk.NSEW)

        self.nome_text_entry.bind('<KeyRelease>', self.eventoTeclado_Nome)

    def entrada_data(self):
        self.data_titulo = LabelcustomizadaTitulo(self.box_frame, text='CAMPO DATA.')
        self.data_titulo.grid(row=5, column=0, sticky=tk.NSEW)

        self.data_label = Labelcustomizada(self.box_frame, text='Digite sua data de nascimento (ex. 23-09-2020):')
        self.data_label.grid(row=6, column=0, sticky=tk.NSEW)

        self.data_text_entry = Text(self.box_frame, width=12, height=1)
        self.data_text_entry.grid(row=6, column=1, sticky=tk.NSEW)

        self.data_status = Labelcustomizada(self.box_frame, wraplength=200)
        self.data_status.grid(row=7, column=0, sticky=tk.NSEW)
        self.data_text_entry.bind('<KeyRelease>', self.eventoTeclado_Data)
        
    def entrada_senha(self):
        self.senha_titulo = LabelcustomizadaTitulo(self.box_frame, text='CAMPO SENHA.')
        self.senha_titulo.grid(row=9, column=0, sticky=tk.NSEW)

        self.senha_label = Labelcustomizada(self.box_frame, text='Digite sua senha:')
        self.senha_label.grid(row=10, column=0, sticky=tk.NSEW)

        self.senha_text_entry = Text(self.box_frame, width=12, height=1)
        self.senha_text_entry.grid(row=10, column=1, sticky=tk.NSEW)

        self.senha_status = Labelcustomizada(self.box_frame, wraplength=200)
        self.senha_status.grid(row=11, column=0, sticky=tk.NSEW)

        self.senha_text_entry.bind('<KeyRelease>', self.eventoTeclado_Senha)

    def eventoTeclado_Nome(self, event):
        pegue_nome = self.nome_get()
        ler_caractere_nome = len(pegue_nome)
        if 5 <= ler_caractere_nome <= 10:
            self.nome_status.config(text=f'Tem {ler_caractere_nome} caracteres!', fg='green')
        elif ler_caractere_nome > 10:
            self.nome_text_entry.config(state=tk.DISABLED)
            Mensagens.msgAtencao(f'Número máximo de caracteres excedido ({ler_caractere_nome})! Resetando o campo nome.')
            self.nome_text_entry.config(state=tk.NORMAL)
            self.nome_text_entry.delete(1.0, tk.END)
            self.nome_status.config(text='Entrada resetada', fg='green')
        else:
            self.nome_status.config(text=f'Tem {ler_caractere_nome} caracteres!', fg='red')
    
    def eventoTeclado_Senha(self, event):
        pegue_senha = self.senha_get()
        ler_caractere_senha = len(pegue_senha)
        if 5 <= ler_caractere_senha <= 10:
            self.senha_status.config(text=f'A sua senha tem {ler_caractere_senha} caracteres!', fg='green')
        elif ler_caractere_senha > 10:
            self.senha_text_entry.config(state=tk.DISABLED)
            Mensagens.msgAtencao(f'Número máximo de caracteres excedido ({ler_caractere_senha})! Resetando o campo senha.')
            self.senha_text_entry.config(state=tk.NORMAL)
            self.senha_text_entry.delete(1.0, tk.END)
            self.senha_status.config(text='Entrada resetada', fg='green')
        else:
            self.senha_status.config(text=f'Sua senha tem {ler_caractere_senha} caracteres. O mínimo é 5 e máximo é 10.', fg='red')

    def formata_data(self):
        try:
            data_formatada = datetime.strptime(self.data_get(), '%d-%m-%Y').date()
            self.data_status.config(text=f'Sua data de nascimento ficou: {data_formatada}.', fg='green')
            return data_formatada
        except ValueError:
            self.data_status.config(text='Insira uma data no formato dd-mm-YYYY', fg='red')
            return None
    
    def eventoTeclado_Data(self, event):
        self.formata_data()
