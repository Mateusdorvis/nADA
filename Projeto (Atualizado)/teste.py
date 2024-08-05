import tkinter as tk

class Cadastro:
    def __init__(self, root):
        self.root = root
        self.root.title('Título do Cadastro')  # Define o título padrão para Cadastro

class Login(Cadastro):
    def __init__(self, root):
        super().__init__(root)
        self.root.title('Login de usuário')  # Sobrescreve o título na classe Login

if __name__ == "__main__":
    root = tk.Tk()  # Cria a instância principal da janela
    app = Login(root)  # Passa a instância principal para a classe Login
    root.mainloop()  # Inicia o loop principal da interface gráfica

