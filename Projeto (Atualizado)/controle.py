import tkinter as tk

from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens
from cadastro import Cadastro
from Salvadados import SalvarUsuario
from datetime import datetime


class Controle:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro()
        self.salvar()

    def salvar(self):
        nome_cadastrado = self.cadastro.nome_get()
        data_cadastrada = self.cadastro.formata_data()
        senha_cadastrada = self.cadastro.senha_get()


        save_users = SalvarUsuario(nome_cadastrado, data_cadastrada, senha_cadastrada)
        print(save_users)


if __name__=='__main__':
    root= tk.Tk()
    app = Controle(root)
    root.mainloop()
        

