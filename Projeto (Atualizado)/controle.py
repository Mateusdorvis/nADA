import tkinter as tk

from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens
from login import Login
from cadastro import Cadastro
from Salvadados import SalvarUsuario
from datetime import datetime


class Controle:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro(self.root)
        self.button_enviar = Buttoncustomizado(self.cadastro.box_frame, text='Enviar cadastro', width=20, command=self.cadastro.enviarCadastro)
        self.button_enviar.grid(row=13, column=0, pady=5, padx=10)

    def salvar_usuario(self):
        nome_cadastrado = self.cadastro.nome_get()
        data_cadastrada = self.cadastro.formata_data()
        senha_cadastrada = self.cadastro.senha_get()
        data = datetime.strptime(data_cadastrada, '%Y-5m-%d')


        save_users = SalvarUsuario(nome_cadastrado, data, senha_cadastrada)
        print(save_users)


if __name__=='__main__':
    root= tk.Tk()
    app = Controle(root)
    root.mainloop()
        

