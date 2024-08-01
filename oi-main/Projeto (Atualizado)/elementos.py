import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MensagensProntas:
    #Não precisa instanciar

    @staticmethod
    def messageErro(mensagem1):
        messagebox.showerror('Erro', mensagem1)
    
    @staticmethod
    def messageInfo(mensagem1):
        messagebox.showinfo('Informação', mensagem1)
    
    @staticmethod
    def messageAlert(mensagem1):
        messagebox.showwarning('Alerta', mensagem1)
    
    @staticmethod
    def messageAviso(mensagem1):
        messagebox.showwarning('Aviso', mensagem1)
    
    @staticmethod
    def messageSimNao(mensagem1):
        return messagebox.askyesno('Escolha uma opção', mensagem1)

def posicao_widget_grid(linha, coluna, widget_escolhido, **keyward):
    widget_escolhido.grid(row=linha, column=coluna, **keyward)
    
class LabelPronta(tk.Label):
    def __init_subclass__(self, master, **keyward):
        super().__init__(master, **keyward)

class EntradaTexto(tk.Text):
    def __init_subclass__(self, master, **keyward):
        super().__init__(master, **keyward)
    
    

        
            
    