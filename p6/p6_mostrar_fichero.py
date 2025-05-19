import os.path

def mostrar_fich(nf: str) -> None:
    with open(os.path.normpath(nf), "r", encoding="utf-8") as fich:
        for linea in fich:
            print(linea, end="")


def main() -> None:
    nf = input("Introduce el nombre del fichero de entrada: ")
    try:
        mostrar_fich(nf)
    except OSError as exc:
        print(f"Error: [{exc!r}]")
        

if __name__ == "__main__":
    main()
