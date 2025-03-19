import math #Chamando a biblioteca math
class CalculoArea:
    def __init__(self,raio):
        self.raio = raio #Armazena o raio dentro do objeto

    def area_circulo(self):
        return math.pi * (raio ** 2)


def main():
    r = float(input("Digite o raio do circulo: "))
    calculo = CalculoArea(r) #criando um objeto de classe
    area = calculo.area_circulo()  #Chamando o método da classe
    print(f"A area do circulo é {area:.2f}m²")


if __name__ == "__main__":
    main()
