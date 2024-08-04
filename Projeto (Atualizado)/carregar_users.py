import mysql.connector
from datetime import datetime

class CarregarUsuario:
    def __init__(self, nome_usuario : str, data_usuario : datetime , senha_usuario : str):
        self.nome_usuario = nome_usuario
        self.data_usuario = data_usuario
        self.senha_usuario = senha_usuario
        self.conexao = mysql.connector.connect(
            host="localhost",       
            user="app",             
            password="oi",         
            database="app_jogos"    
        )
        self.cursor = self.conexao.cursor()
        self.criar_tabela_dados_usuarios()
        self.inserir_usuario_nas_tabelas()
        self.show_users()
        self.conexao.commit()
        self.conexao.close()
        

  
