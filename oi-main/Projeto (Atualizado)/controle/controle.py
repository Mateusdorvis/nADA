import tkinter as tk
from tkinter import ttk
from view.elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens
from view.login import Login
from view.cadastro import Cadastro
from modelo.Salvadados import SalvarUsuario

class Controle:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro(self.root)
        self.nome_cadastrado = self.cadastro.nome_get()
        self.data_cadastrada = 
        pass
    
    def salvar_usuario(self):
        save_users = SalvarUsuario()

        

