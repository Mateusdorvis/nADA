import tkinter as tk
from datetime import datetime
from tkinter import Widget, ttk
from tkinter import messagebox
from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens, Framecustomizado, Textcustomizado

class BaseCadastro:
    def __init__(self):
        self.root = tk.Tk()
        self.frame_caixa = Framecustomizado(self.root)
        self.frame_caixa.grid(row=0, column=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.frame_caixa.grid_columnconfigure(0, weight=1)
        for linha in range(20):
             self.frame_caixa.grid_rowconfigure(linha+1, weight=1)
        self.root.config(bg='#0ba18c')
        self.entrada_nome()
        self.entrada_senha()
        self.entrada_data()
        self.root.mainloop()
    
    def entrada_nome(self):
        self.nome_titulo = LabelcustomizadaTitulo(self.frame_caixa, text='CAMPO NOME.')
        self.nome_titulo.grid(row=0, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_label = Labelcustomizada(self.frame_caixa, text='Digite seu nome :')
        self.nome_label.grid(row=1, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_entrada = Textcustomizado(self.frame_caixa)
        self.nome_entrada.grid(row=1, column=1, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_dicas = Labelcustomizada(self.frame_caixa)
        self.nome_dicas.grid(row=2, column=0, sticky=tk.NSEW, pady=5, padx=5)
    
    def entrada_senha(self):
        self.senha_titulo = LabelcustomizadaTitulo(self.frame_caixa, text='CAMPO SENHA.')
        self.senha_titulo.grid(row=3, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_label = Labelcustomizada(self.frame_caixa, text='Digite sua senha :')
        self.senha_label.grid(row=4, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_entrada = Textcustomizado(self.frame_caixa)
        self.senha_entrada.grid(row=4, column=1, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_dicas = Labelcustomizada(self.frame_caixa)
        self.senha_dicas.grid(row=5, column=0, sticky=tk.NSEW, pady=5, padx=5)
    
    def entrada_data(self):
        self.data_titulo = LabelcustomizadaTitulo(self.frame_caixa, text='CAMPO DATA.')
        self.data_titulo.grid(row=6, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.data_label = Labelcustomizada(self.frame_caixa, text='Digite sua data de nascimento no formato dd-mm-YYYY :', justify='left')
        self.data_label.grid(row=7, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.data_entrada = Textcustomizado(self.frame_caixa)
        self.data_entrada.grid(row=7, column=1, sticky=tk.NSEW, pady=5, padx=5)

        self.data_dicas = Labelcustomizada(self.frame_caixa)
        self.data_dicas.grid(row=8, column=0, sticky=tk.NSEW, pady=5, padx=5)


BaseCadastro()
        


        