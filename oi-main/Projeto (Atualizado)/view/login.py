import tkinter as tk
from tkinter import ttk
from elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Buttoncustomizado
from cadastro import Cadastro

class Login(Cadastro):
    def __init__(self, root):
        super().__init__(root)
        del self.entrada_data()
        del self.data_get()
        del self.eventoTeclado_Data()

if __name__=='__main__':
    root = tk.Tk()
    login = Login(root)



        