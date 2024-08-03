import tkinter as tk

from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens
from login import Login
from cadastro import Cadastro
from Salvadados import SalvarUsuario


class Controle:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro(self.root)

    def salvar_usuario(self):
        nome_cadastrado = self.cadastro.nome_get()
        senha_cadastrada = self.cadastro.senha_get()

        save_users = SalvarUsuario(nome_cadastrado,  senha_cadastrada)

if __name__=='__main__':
    root= tk.Tk()
    app = Controle(root)
    root.mainloop()
        

