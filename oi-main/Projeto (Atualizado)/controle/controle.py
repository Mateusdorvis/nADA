from view.elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens
from view.login import Login
from view.cadastro import Cadastro
from modelo.Salvadados import SalvarUsuario


class Controle:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro(self.root)

    def salvar_usuario(self):
        nome_cadastrado = self.cadastro.nome_get()
        data_cadastrada = self.cadastro.data_get()
        senha_cadastrada = self.cadastro.senha_get()

        save_users = SalvarUsuario(nome_cadastrado, data_cadastrada, senha_cadastrada)

if __name__=='__main__':
    root= tk.Tk()
    app = Controle(root)
    root.mainloop()
        

