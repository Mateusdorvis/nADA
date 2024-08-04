import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Mensagens:
  @staticmethod

  def msgAtencao(msg):
    messagebox.showwarning('Atenção', msg)
    
  @staticmethod
  def msgInfo(msg):
    messagebox.showinfo('Informação', msg)

def titulo(titulo, master,linha,  **args,):
  label = tk.Label(master, **args)
  label.grid(row=linha, column=0, sticky=tk.NSEW)

#label para textos etc.
def Labelcustomizada(master, **args):
  args.setdefault('bg', 'white')
  args.setdefault('font', ('Courier New', 9))
  return tk.Label(master, wraplength=200, **args)

#label dedicada a titulos
def LabelcustomizadaTitulo(master, **args):
  args.setdefault('bg', '#ebeaef')
  args.setdefault('font', ('Courier New', 12, 'bold'))
  return tk.Label(master, **args)


#label dedicada a titulos
def Buttoncustomizado(master, **args):
  args.setdefault('bg', 'black')
  args.setdefault('fg', 'white')
  args.setdefault('font', ('Courier New', 9, 'bold'))
  return tk.Button(master, **args)

def Framecustomizado(master, **args):
  args.setdefault('bg', 'white')
  return tk.Frame(master, width=1000, height=500, **args)

def Textcustomizado(master, **args):
  args.setdefault('width', '12')
  args.setdefault('height', '0')
  return tk.Text(master, **args)
                    
                    

