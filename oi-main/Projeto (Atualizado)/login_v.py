import tkinter as tk
from  tkinter import ttk
from datetime import datetime
from elementos import MensagensProntas
class Login:
     def __init__(self, funcao):
        self.funcao = funcao
        self.root = tk.Tk()
        self.root.title('Cadastro')
        self.root.resizable(False, False)
        self.contar_click = 0
        self.aparecer_nome_cadastro()
        self.aparecer_senha_cadastro()
        self.Enviar_dados()
        self.root.grid_columnconfigure(0, weight=1)
        for x in range(14):
            self.root.grid_rowconfigure(x, weight=1)
    
     def aparecer_nome_cadastro(self):
        self.nome_titulo = tk.Label(self.root, text='1 -NOME DO USUÁRIO', font=12)
        self.nome_titulo.grid(row=0, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_label = tk.Label(self.root, text='Digite seu nome :')
        self.nome_label.grid(row=1, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_entrada = tk.Text(self.root, height=0, width=15)
        self.nome_entrada.grid(row=2, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_label_status = tk.Label(self.root)
        self.nome_label_status.grid(row=3, column=0, sticky=tk.NSEW, pady=5, padx=5)
        
        def eventos_nome_entrada(event):
            
            ler_nome = len(self.nome_entrada.get(1.0,tk.END))

            if ler_nome<=6:
                self.nome_label_status.config(text=f'Tem {ler_nome} caracteres!',fg='red')
                if ler_nome<=1:
                        self.nome_label_status.config(text=f' Tem  {ler_nome} caractere!',fg='red')


            elif ler_nome>=12:
                self.nome_label_status.config(text=f'Atingiu números de caracteres máximo !',fg='red')
                self.nome_entrada.config(state='disabled')
                resposta = MensagensProntas.messageSimNao('Deseja resetar a entrada ?')
                if resposta:
                    self.nome_label_status.config(text='')
                    self.nome_entrada.config(state='normal')
                    self.nome_entrada.delete(1.0, tk.END)
                    
            else:
                self.nome_label_status.config(text=f'Você atingiu números de caracteres mínimo, pois tem {ler_nome}',fg='green')
                questao = MensagensProntas.messageSimNao(f"Tem certeza que você entrou com esse nome no app ? '{self.nome_entrada.get(1.0,tk.END)}'?")
                if questao:
                    self.nome_entrada.config(state='disabled')


        self.nome_entrada.bind('<KeyRelease>', eventos_nome_entrada)

    
     def aparecer_senha_cadastro(self):
        self.senha_titulo = tk.Label(self.root, text='3 - SENHA ', font=12)
        self.senha_titulo.grid(row=4, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_label = tk.Label(self.root, text='Digite sua sneha :')
        self.senha_label.grid(row=5, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_entrada = tk.Text(self.root, height=0, width=15)
        self.senha_entrada.grid(row=6, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_label_status = tk.Label(self.root)
        self.senha_label_status.grid(row=7, column=0, sticky=tk.NSEW, pady=5, padx=5)

        def eventos_senha_entrada(event):
            ler_senha = len(self.senha_entrada.get(1.0, tk.END).strip())
            if ler_senha>=8:
                self.senha_label_status.config(text=f'A senha passou de 8 caracteres, você digitou {ler_senha} caracteres !', fg='red')
                self.data_entrada.config(state='disabled')

            elif ler_senha<=4:

                self.senha_label_status.config(text=f'A senha é no máximo 8 caracteres. \n Você digitou {ler_senha} caracteres e falta + {8-ler_senha} caracteres !')

                if ler_senha<=1:
                    self.senha_label_status.config(text=f'A senha é no máximo 8 caracteres. \n Você digitou {ler_senha} caractere e falta + {8-ler_senha} caracteres !', fg='red')
                    

            else:
                self.senha_label_status.config(text=f'Você atingiu número  mínimo de caracteres !', fg='green')
                questao = MensagensProntas.messageSimNao(f"Tem certeza que deseja entrar com esta senha :   '{self.senha_entrada.get(1.0, tk.END).strip()}' ?")
                if questao:
                    self.senha_entrada.config(state='disabled')
                

        self.senha_entrada.bind('<KeyRelease>', eventos_senha_entrada)

     def Enviar_dados(self):
        def Verifiicar_campos():
            nome_get = self.nome_entrada.get(1.0, tk.END).strip()
            senha_get = self.senha_entrada.get(1.0, tk.END).strip()
           

            def voltar_para_janela_principal():
             
              
              
                self.root.destroy()

            #condição campos vazios
            if nome_get=='' and    senha_get=='' :
                MensagensProntas.messageAviso('Precnha os campos por favor , eles estão vazios!')
            elif senha_get=='':
                    MensagensProntas.messageAviso('  O campo SENHA está vazio,preencha por favor !')
            elif nome_get=='':
                    MensagensProntas.messageAviso('  O campo NOME está vazio,preencha por favor !')

                
            #CONDIÇÃO STATUS
            elif self.nome_label_status.cget('fg')=='red'  and  self.senha_label_status.cget('fg')=='red':
                MensagensProntas.messageAviso('Precnha os campos por favor !')

            elif self.senha_label_status.cget('fg')=='red':
                    MensagensProntas.messageAviso(' Preencha o campo SENHA, por favor !')
                    
            elif self.nome_label_status.cget('fg')=='red':
                    MensagensProntas.messageAviso(' Preencha o campo NOME, por favor !')
            #CONDICÇÃO STATUS E ESPAÇO VAZIO:
            else:
                    try:
                        with open('C:\\Users\\mateu\\Downloads\\oi2-main\\python\\oi\\oi-main\\Projeto (Atualizado)\\save_dados.txt', 'r') as arquivo:
                            senha_encontrada = None
                            nome_encontrado = False
                            for cada_linha in arquivo:
                                cada_linha = cada_linha.strip() 

                                if cada_linha.startswith('Nome :'):
                                    nome = cada_linha[len('Nome :'):].strip()
                                    if nome == nome_get:
                                        nome_encontrado = True
                                        
                                elif cada_linha.startswith('Senha :'):
                                    senha = cada_linha[len('Senha :'):].strip()
                                    if nome_encontrado:
                                        senha_encontrada = senha
                                        if senha_encontrada!=senha:
                                            MensagensProntas.messageAviso(f' Sua senha {nome_get} está incorreta !')
                                            self.nome_entrada.config(state=tk.NORMAL)
                                            self.nome_entrada.delete(1.0,tk.END)
                                            self.senha_entrada.config(state=tk.NORMAL)
                                            self.senha_entrada.delete(1.0,tk.END)

                                elif cada_linha.startswith('Data de nascimento : '):
                                        data_nascimento = cada_linha[len('Data de nascimento : '):].strip()
                                        MensagensProntas.messageInfo(f'Cadastro realizado com sucesso {nome_get} !')
                                        self.funcao(nome_get, senha_get, data_nascimento)
                                        voltar_para_janela_principal()
                                        self.contar_click+=1
                                        if self.contar_click>=2:
                                            
                                            MensagensProntas.messageAviso(f' Você já está logado {nome_get}  !')
                                        break  
                                
                            if not nome_encontrado:
                                MensagensProntas.messageAviso(f' Seu nome {nome_get} não foi encontrado !')
                                self.nome_entrada.config(state=tk.NORMAL)
                                self.nome_entrada.delete(1.0,tk.END)

                                self.senha_entrada.config(state=tk.NORMAL)
                                self.senha_entrada.delete(1.0,tk.END)

                        
                    except FileNotFoundError:
                        MensagensProntas.messageAviso('  O campo NOME está vazio,preencha por favor !')


             
               

        self.button_enviar = tk.Button(self.root,text='Enviar', command=Verifiicar_campos)
        self.button_enviar.grid(row=8, column=0, sticky=tk.NSEW, pady=5, padx=5)
        
        def Verificar_senha():
            nome_pocurado = tk.Label(self.root, text='Digite seu nome : ')
            nome_pocurado.grid(row=10, column=0, pady=5, padx=5)

            verificar_nome = tk.Entry(self.root)
            verificar_nome.grid(row=11, column=0, pady=5, padx=5)
            
           
            def check_user():
                get_nome = verificar_nome.get()
                try:
                    with open('C:\\Users\\mateu\\Downloads\\oi2-main\\python\\oi\\oi-main\\Projeto (Atualizado)\\save_dados.txt', 'r') as arquivo:
                     senha_encontrada = None
                    
                     for cada_linha in arquivo:
                        cada_linha = cada_linha.strip() 
                        
                        if cada_linha.startswith('Nome :'):
                            nome = cada_linha[len('Nome :'):].strip()
                            if nome == get_nome:
                                nome_encontrado = True
                                text = tk.Label(self.root, text=f'Nome: {nome}')
                                text.grid(row=14, column=0, pady=5, padx=5)
                        
                        elif cada_linha.startswith('Senha :'):
                            senha = cada_linha[len('Senha :'):].strip()
                            if nome_encontrado:
                                senha_encontrada = senha
                                text2 = tk.Label(self.root, text=f'Senha: {senha}')
                                text2.grid(row=15, column=0, pady=5, padx=5)
                                break 

                    if not nome_encontrado:

                        label = tk.Label(self.root, text='Não consegui te encontrar !')
                        label.grid(row=16, column=0, columnspan=2, pady=5, padx=5)
                    
                except FileNotFoundError:
                    label1 =tk.Label(self.root, text='Arquivo não encontrado!')
                    label1.grid(row=17, column=0, columnspan=2, pady=5, padx=5)


            button_check = tk.Button(self.root, text='Checar', command=check_user)
            button_check.grid(row=12, column=0, pady=5, padx=5)
           
        self.button_esqueci_senha = tk.Button(self.root,text='Esqueci a senha', command=Verificar_senha)
        self.button_esqueci_senha.grid(row=9, column=0, sticky=tk.NSEW, pady=5, padx=5)
