
def calc_media(n: int) -> None:
    sum: float = 0
    for i in range(1, n+1):
        sum += float(input(f"Precio modelo {i}: "))
    print(f"El valor medio de los {n} modelos de coche asciende a: {sum/n} €")


def main() -> None:
    n = int(input("Introduzca cantidad de modelos de coche: "))
    
    if (n > 0):
        calc_media(n)
    else:
        print("Error")
        

if __name__ == "__main__":
    main()