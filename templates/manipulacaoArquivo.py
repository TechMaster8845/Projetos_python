'''
Template
Útil para: Criar, ler e modificar arquivos
'''


def escrever_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

def main():
    nome = "exemplo.txt"
    escrever_arquivo(nome, "Este é um exemplo de arquivo.")
    conteudo = ler_arquivo(nome)
    if conteudo:
        print("Conteúdo do arquivo:", conteudo)

if __name__ == "__main__":
    main()
