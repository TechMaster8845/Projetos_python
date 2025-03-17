def converter_medidas(metros):
    centimetros = metros * 100
    milimetros = metros * 1000
    return centimetros, milimetros


def main():
    x = float(input("Digite um nùmeron em metros: "))
    cm, mm = converter_medidas(x)
    print(f"{x} metros equivalem a {cm} centímetros e {mm} milímetros.")


if __name__ == "__main__":
    main()
