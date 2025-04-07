def leer_numero(mensaje: str) -> (int|float):
    entrada = input(mensaje)
    num = float(entrada)
    if num // 1 == num:
        num = int(num)
    return num


def main() -> None:
    try:
        num = leer_numero("Introduce un numero: ")
        print(f"Numero: {num}")
    except ValueError as exc:
        print(f"Error: [{exc!r}]")


if __name__ == "__main__":
    main()