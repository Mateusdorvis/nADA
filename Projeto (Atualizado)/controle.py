import tkinter as tk
from elementos_tkinter import Buttoncustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Textcustomizado
from sistema_login import Registro
from modelo import SalvarUsuario, CarregarUsuario

class Controle:
    def __init__(self, root):
        self.root = root
        self.registro = Registro(root)
     
        self.registro.button_enviar.config(command=self.salvar_usuario)
        
    
    
    def salvar_usuario(self):
        self.nome = self.registro.nome_get()
        self.senha = self.registro.senha_get()
        self.data = self.registro.data_get()
        


root = tk.Tk()
x = Controle(root)
root.mainloop()
    
        
        