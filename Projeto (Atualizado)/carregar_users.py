import mysql.connector
from datetime import datetime

class CarregarUsuario:
    def __init__(self,  : str, data_usuario : datetime , senha_usuario : str):
        self.conexao = mysql.connector.connect(
            host="localhost",       
            user="app",             
            password="oi",         
            database="app_jogos"    
        )
        self.cursor = self.conexao.cursor()
        self.show_users()
        self.conexao.commit()
        self.conexao.close()
    
    def show_users(self):
        self.cursor.execute("SELECT * FROM dados_usuarios;")
        self.mostrar_usuarios = self.cursor.fetchall()
        self.dicio_pessoa = {}
        contar = 0
        for usuario in self.mostrar_usuarios:
            self.dicio_pessoa[f'usuário {contar + 1} '] = {'ID': usuario[0],
            'Nome' :  usuario[1], 
            'Data de nascimento ': usuario[2], 
            'Senha'  : usuario[3]
            }
            print(self.dicio_pessoa)
        

  
