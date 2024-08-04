import tkinter as tk
from datetime import datetime
from tkinter import Widget, ttk
from tkinter import messagebox
from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens, Framecustomizado, Textcustomizado

class BaseCadastro:
    def __init__(self):
        self.root = tk.Tk()
        self.frame_caixa = Framecustomizado(self.root, width=300, height=300)
        self.frame_caixa.grid(row=0, column=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.frame_caixa.grid_columnconfigure(0, weight=1)
        for linha in range(20):
             self.frame_caixa.grid_rowconfigure(linha, weight=1)
        self.root.config(bg='#0ba18c')
        self.entrada_nome()
        self.root.mainloop()
    
    def entrada_nome(self):
        self.nome_titulo = LabelcustomizadaTitulo(self.frame_caixa, text='CAMPO NOME.')
        self.nome_titulo.grid(row=0, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_label = Labelcustomizada(self.frame_caixa, text='Digite seu nome')
        self.nome_label.grid(row=1, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_entrada = Textcustomizado(self.frame_caixa)
        self.nome_entrada.grid(row=1, column=1, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_dicas = Labelcustomizada(self.frame_caixa)
        self.nome_dicas.grid(row=2, column=0, sticky=tk.NSEW, pady=5, padx=5)


BaseCadastro()
        


        