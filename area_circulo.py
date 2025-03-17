import math

def area_circulo(raio):
    return math.pi * (raio ** 2)


def main():
    r = float(input("Digite o raio do circulo: "))
    area = area_circulo(r)
    print(f"A area do circulo é {area:.2f}m²")


if __name__ == "__main__":
    main()
