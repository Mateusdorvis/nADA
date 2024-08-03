import mysql.connector
from datetime import datetime

class SalvarUsuario:
    def __init__(self, nome_usuario : str, data_usuario : datetime, senha_usuario : str):
        self.nome_usuario = nome_usuario
        self.data_usuario = data_usuario
        self.senha_usuario = senha_usuario
        self.conexao = mysql.connector.connect(
            host="localhost",       
            user="mateus",             
            password="oi",         
            database="formulario"    
        )
        self.cursor = self.conexao.cursor()
        self.criar_tabela_dados_usuarios()
        self.inserir_usuario_nas_tabelas()
        self.provar_que_os_usuarios_foram_inseridos()
        self.conexao.commit()
        self.conexao.close()
        

    def criar_tabela_dados_usuarios(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dados_usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome_usuarios VARCHAR(255) NOT NULL,
                datas_de_nascimentos DATE,
                senhas_usuarios VARCHAR(255) NOT NULL
            );
            """)
            print(f' Tabela criada com sucesso !')
        except ValueError:
            print(f'Erro ao criar tabela !')

    def inserir_usuario_nas_tabelas(self):
        try:
            self.cursor.execute( """
            INSERT INTO dados_usuarios (nome_usuarios, datas_de_nascimentos, senhas_usuarios)
            VALUES (%s, %s, %s);
            """, (self.nome_usuario, self.data_usuario, self.senha_usuario))
                
            if self.nome_usuario.endswith('a'):
                print(f' A Usuária {self.nome_usuario} foi inserida na tabela com sucesso !')
            else:
                print(f' O Usuário {self.nome_usuario} foi inserido na tabela com sucesso !')


        except ValueError:
            print(f'Erro ao inserir o usuário {self.nome_usuario} !')

    def provar_que_os_usuarios_foram_inseridos(self):
        self.cursor.execute("SELECT * FROM dados_usuarios;")
        mostrar_usuarios = self.cursor.fetchall()
        print(mostrar_usuarios)

    
        
        