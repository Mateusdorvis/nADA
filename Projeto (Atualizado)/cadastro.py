import tkinter as tk
from datetime import datetime
from tkinter import Widget, ttk
from tkinter import messagebox
from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens



class Cadastro:

    def __init__(self, root):
        self.root = root
        #self.root.resizable(False, False)
        self.root.title('Cadastro de usuário')
        self.root.config(bg='#2f6f8e')
        self.entrada_nome()
        self.contar = 0
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.entrada_data()
        self.entrada_senha()
    
  
   
            
    
   
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


    def entrada_data(self):
        self.data_titulo = LabelcustomizadaTitulo(self.box_frame,
                                    text='CAMPO DATA.')
        self.data_titulo.grid(row=5, column=0, sticky=tk.NSEW)

        self.data_label = Labelcustomizada(self.box_frame, text='Digite sua data de nascimento (ex. 23-09-2020) :')
        self.data_label.grid(row=6, column=0, sticky=tk.NSEW)

        self.data_text_entry = tk.Text(self.box_frame, width=12, height=0)
        self.data_text_entry.grid(row=6, column=1, sticky=tk.NSEW)

        self.data_status = Labelcustomizada(self.box_frame, wraplength=200)
        self.data_status.grid(row=7, column=0, sticky=tk.NSEW)
   

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

    

       
        

        
        
        