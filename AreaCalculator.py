"""
Este programa calcula area de formas
geometricas conhecidas na Engenharia civil.
"""
import math

class CalculoArea:
    def __init__(self, raio=None, lado=None, largura=None, comprimento=None,
                 base=None, altura=None, base_maior=None, base_menor=None,
                 diagonal_maior=None, diagonal_menor=None, eixo_maior=None,
                 eixo_menor=None):
        self.raio = raio
        self.lado = lado
        self.largura = largura
        self.comprimento = comprimento
        self.base = base
        self.altura = altura
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.diagonal_maior = diagonal_maior
        self.diagonal_menor = diagonal_menor
        self.eixo_maior = eixo_maior
        self.eixo_menor = eixo_menor

    def area_circulo(self):
        return math.pi * (self.raio ** 2) if self.raio else None

    def area_quadrado(self):
        return self.lado ** 2 if self.lado else None

    def area_retangulo(self):
        return self.largura * self.comprimento if self.largura and self.comprimento else None

    def area_triangulo(self):
        return (self.base * self.altura) / 2 if self.base and self.altura else None

    def area_trapezio(self):
        return ((self.base_maior + self.base_menor) * self.altura) / 2 if self.base_maior and self.base_menor and self.altura else None

    def area_losango(self):
        return (self.diagonal_maior * self.diagonal_menor) / 2 if self.diagonal_maior and self.diagonal_menor else None

    def area_paralelogramo(self):
        return self.base * self.altura if self.base and self.altura else None

    def area_elipse(self):
        return math.pi * self.eixo_maior * self.eixo_menor if self.eixo_maior and self.eixo_menor else None

    def area_hexagono(self):
        return ((3 * math.sqrt(3)) / 2) * (self.lado ** 2) if self.lado else None

def main():
    print("\nEscolha a figura geométrica para calcular a área:")
    print("1 - Círculo")
    print("2 - Quadrado")
    print("3 - Retângulo")
    print("4 - Triângulo")
    print("5 - Trapézio")
    print("6 - Losango")
    print("7 - Paralelogramo")
    print("8 - Elipse")
    print("9 - Hexágono Regular")

    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        r = float(input("Digite o raio do círculo: "))
        calculo = CalculoArea(raio=r)
        print(f"A área do círculo é {calculo.area_circulo():.2f} m²")

    elif opcao == "2":
        l = float(input("Digite o lado do quadrado: "))
        calculo = CalculoArea(lado=l)
        print(f"A área do quadrado é {calculo.area_quadrado():.2f} m²")

    elif opcao == "3":
        largura = float(input("Digite a largura do retângulo: "))
        comprimento = float(input("Digite o comprimento do retângulo: "))
        calculo = CalculoArea(largura=largura, comprimento=comprimento)
        print(f"A área do retângulo é {calculo.area_retangulo():.2f} m²")

    elif opcao == "4":
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        calculo = CalculoArea(base=base, altura=altura)
        print(f"A área do triângulo é {calculo.area_triangulo():.2f} m²")

    elif opcao == "5":
        base_maior = float(input("Digite a base maior do trapézio: "))
        base_menor = float(input("Digite a base menor do trapézio: "))
        altura = float(input("Digite a altura do trapézio: "))
        calculo = CalculoArea(base_maior=base_maior, base_menor=base_menor, altura=altura)
        print(f"A área do trapézio é {calculo.area_trapezio():.2f} m²")

    elif opcao == "6":
        diagonal_maior = float(input("Digite a diagonal maior do losango: "))
        diagonal_menor = float(input("Digite a diagonal menor do losango: "))
        calculo = CalculoArea(diagonal_maior=diagonal_maior, diagonal_menor=diagonal_menor)
        print(f"A área do losango é {calculo.area_losango():.2f} m²")

    elif opcao == "7":
        base = float(input("Digite a base do paralelogramo: "))
        altura = float(input("Digite a altura do paralelogramo: "))
        calculo = CalculoArea(base=base, altura=altura)
        print(f"A área do paralelogramo é {calculo.area_paralelogramo():.2f} m²")

    elif opcao == "8":
        eixo_maior = float(input("Digite o eixo maior da elipse: "))
        eixo_menor = float(input("Digite o eixo menor da elipse: "))
        calculo = CalculoArea(eixo_maior=eixo_maior, eixo_menor=eixo_menor)
        print(f"A área da elipse é {calculo.area_elipse():.2f} m²")

    elif opcao == "9":
        lado = float(input("Digite o lado do hexágono regular: "))
        calculo = CalculoArea(lado=lado)
        print(f"A área do hexágono é {calculo.area_hexagono():.2f} m²")

    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
