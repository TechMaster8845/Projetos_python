'''
Template
Útil para: Criar e consultar bancos de dados localmente
'''
import sqlite3

def criar_banco():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL)''')
    conexao.commit()
    conexao.close()

def inserir_usuario(nome):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

def main():
    criar_banco()
    inserir_usuario("Alice")
    inserir_usuario("Bob")
    print("Usuários cadastrados:", listar_usuarios())

if __name__ == "__main__":
    main()
