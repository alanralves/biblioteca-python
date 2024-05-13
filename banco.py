# Importa a biblioteca sqlite3
import sqlite3

class Banco(): # Cria a classe banco

    def __init__(self): # Cria o construtor da classe banco
        self.conn = sqlite3.connect('biblioteca.db') # Cria o banco de dados da biblioteca
        self.createTableUsuarios() # Chama o método que cria a tabela usuários
        self.createTableLivros() # Chama o método que cria a tabela livros

    def createTableUsuarios(self): # Método de criação da tabela usuários
        cursor = self.conn.cursor() # Cria a conexão com o banco de dados
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT , nome TEXT NOT NULL, telefone TEXT NOT NULL, email TEXT NOT NULL);""") # Cria a tabela usuarios caso não tenha sido criada
        self.conn.commit() # Grava as informações no banco de dados
        cursor.close() # Fecha a conxão com o banco de dados

    def createTableLivros(self): # Método de criação da tabela usuários
        cursor = self.conn.cursor() # Cria a conexão com o banco de dados
        cursor.execute("""CREATE TABLE IF NOT EXISTS livros (titulo TEXT NOT NULL, autor TEXT NOT NULL, ano INTEGER NOT NULL, quantidade INTEGER NOT NULL);""") # Cria a tabela livros caso não tenha sido criada
        self.conn.commit() # Grava as informações no banco de dados
        cursor.close() # Fecha a conxão com o banco de dados

    def select(self,query): # Método de seleção de informações
        cursor = self.conn.cursor() # Cria a conexão com o banco de dados
        cursor.execute(query) # Executa a pesquisa recebida como parametro
        resultado = cursor.fetchall() # Retorna o resultado da pesquisa
        cursor.close() # Fecha a conxão com o banco de dados
        return resultado
    
    def selectUpdate(self,query): # Método de seleção de informações a serem atualizadas
        cursor = self.conn.cursor() # Cria a conexão com o banco de dados
        cursor.execute(query) # Executa a pesquisa recebida como parametro
        resultado = cursor.fetchone() # Retorna uma única linha como resultado da pesquisa
        cursor.close() # Fecha a conxão com o banco de dados
        return resultado
    
    def change(self,query): # Método de atualização de informações
        try: # Inicia o tratamento de erro
            cursor = self.conn.cursor() # Cria a conexão com o banco de dados
            cursor.execute(query) # Executa a pesquisa recebida como parametro
            cursor.connection.commit() # Grava as informações no banco de dados
            cursor.close() # Fecha a conxão com o banco de dados
        except Exception as e: # Executa caso ocorra erro
            print(e)




        