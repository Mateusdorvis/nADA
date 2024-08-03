import tkinter as tk
from tkinter import ttk
from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Buttoncustomizado
from cadastro import Cadastro

class Login(Cadastro):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title('Login de usuário')
    
    def entrada_data(self):
        pass

    def eventoTeclado_Data(self, event):
        pass

    def data_get(self):
        pass

if __name__=='__main__':
    root = tk.Tk()
    login = Login(root)



        