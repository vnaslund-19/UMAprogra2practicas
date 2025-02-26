def es_primo(numero: int) -> bool:
    if numero == 2:
        res = True
    elif numero % 2 == 0 or numero <= 1:
        res = False
    else:
        res = True
        for i in range(3, numero//2, 2):
            if numero % i == 0:
                res = False
    return res

def print_primes(l: int, u: int) -> None:
    for i in range(l, u+1):
        if (es_primo(i)):
            print(i, end=" ")
    print()


def main() -> None:
    l = int(input("Introduce el número menor del intervalo: "))
    u = int(input("Introduce el número mayor del intervalo: "))

    if (u > l and l > 0):
        print_primes(l, u)
    else:
        print("Error")


if __name__ == "__main__":
    main()