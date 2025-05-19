import os.path

def cargar_fich(nf: str) -> None:
    linea = input("Introduce líneas de texto (hasta línea vacía):")
    with open(os.path.normpath(nf), "w", encoding="utf-8") as fich:
        while linea != "":
            fich.write(linea)
            fich.write("\n")
            linea = input()


def main() -> None:
    nf = input("Introduce el nombre del fichero de salida: ")
    try:
        cargar_fich(nf)
    except OSError as exc:
        print(f"Error: [{exc!r}]")
        

if __name__ == "__main__":
    main()