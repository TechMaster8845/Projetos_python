'''
Template
Útil para: Programação Orientada a Objetos (POO)
'''

class MinhaClasse:
    def __init__(self, atributo):
        self.atributo = atributo  # Atributo da instância

    def mostrar_atributo(self):
        print(f"Atributo: {self.atributo}")

def main():
    obj = MinhaClasse("Exemplo")
    obj.mostrar_atributo()

if __name__ == "__main__":
    main()
