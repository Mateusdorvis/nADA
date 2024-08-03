import tkinter as tk

from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens
from cadastro import Cadastro
from Salvadados import SalvarUsuario
from datetime import datetime


class Controle:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro(self.root)

        self.salvar()

    def salvar(self):
       

        save_users = SalvarUsuario(self.cadastro.nome_get(),self.cadastro.formata_data() ,self.cadastro.senha_get(
        ) )
        print(save_users)


if __name__=='__main__':
    root= tk.Tk()
    app = Controle(root)
    root.mainloop()
        

