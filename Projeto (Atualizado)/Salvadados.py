import mariadb
from datetime import datetime

class SalvarUsuario:
    def __init__(self, nome_usuario, data_usuario, senha_usuario):
        self.nome_usuario = nome_usuario
        self.data_usuario = data_usuario
        self.senha_usuario = senha_usuario

        try:
            self.conexao = mariadb.connect(
                host="localhost",
                user="app",
                password="oi",
                database="app_jogos"
            )
            self.cursor = self.conexao.cursor()
            self.criar_tabela_dados_usuarios()
            self.inserir_usuario_nas_tabelas()
            self.provar_que_os_usuarios_foram_inseridos()
            self.conexao.commit()
        except mariadb.Error as e:
            print(f"Erro ao conectar ao MariaDB: {e}")
        finally:
            if self.conexao:
                self.conexao.close()
                print('Conexão com o banco de dados fechada.')

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
            print('Tabela criada com sucesso!')
        except mariadb.Error as e:
            print(f'Erro ao criar tabela: {e}')

    def inserir_usuario_nas_tabelas(self):
        try:
            # Converte a data para o formato adequado se necessário
            data_formatada = datetime.strptime(self.data_usuario, '%d-%m-%Y').date()

            self.cursor.execute("""
            INSERT INTO dados_usuarios (nome_usuarios, datas_de_nascimentos, senhas_usuarios)
            VALUES (%s, %s, %s);
            """, (self.nome_usuario, data_formatada, self.senha_usuario))

            if self.nome_usuario.endswith('a'):
                print(f'A Usuária {self.nome_usuario} foi inserida na tabela com sucesso!')
            else:
                print(f'O Usuário {self.nome_usuario} foi inserido na tabela com sucesso!')
        except mariadb.Error as e:
            print(f'Erro ao inserir o usuário {self.nome_usuario}: {e}')

    def provar_que_os_usuarios_foram_inseridos(self):
        try:
            self.cursor.execute("SELECT * FROM dados_usuarios;")
            mostrar_usuarios = self.cursor.fetchall()
            print(mostrar_usuarios)
        except mariadb.Error as e:
            print(f'Erro ao buscar usuários: {e}')
