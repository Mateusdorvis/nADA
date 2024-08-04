from cadastro import Cadastro
from tkinter import ttk
import tkinter as tk

class Login(Cadastro):
    def __init__(self, root):
        super().__init__(root)
        self.root.title('Login de usuário')
    
    def entrada_data(self):
        pass
root = tk.Tk()
login = Login(root)
root.mainloop()
