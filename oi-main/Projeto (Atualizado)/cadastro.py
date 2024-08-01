import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import elementos

class Cadastro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Cadastro')

    def coletar_dados(self):
        self.nome_titulo = tk.Label(self.root, bg='white', text='NOME')
        self.nome_titulo.grid()
        
        