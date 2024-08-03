import tkinter as tk
from cadastro import Cadastro
from SalvarUsuario import SalvarUsuario
from elementos_tkinter import Buttoncustomizado, Mensagens

class Controle:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro(self.root)
        
        # Adiciona o botão 'Salvar Usuário' usando grid
        self.button_salvar = Buttoncustomizado(self.root, text='Salvar Usuário', command=self.salvar_usuario)
        self.button_salvar.grid(row=1, column=0, pady=10, padx=10)

    def salvar_usuario(self):
        nome_cadastrado = self.cadastro.nome_get()
        data_cadastrada = self.cadastro.formata_data()
        senha_cadastrada = self.cadastro.senha_get()

        if data_cadastrada:
            save_users = SalvarUsuario(nome_cadastrado, data_cadastrada, senha_cadastrada)
            print('Usuário salvo com sucesso!')
        else:
            Mensagens.msgAtencao('Data inválida. O usuário não foi salvo.')

if __name__ == '__main__':
    root = tk.Tk()
    app = Controle(root)
    root.mainloop()
