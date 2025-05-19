import os.path

class Reemplazar:
    def __init__(self, *args, **kwargs) -> None:
        self.__reemplazos = dict()
        super().__init__(*args, **kwargs)
    
    def anyadir(self, texto: str, sust: str) -> None:
        self.__reemplazos[texto] = sust
    
    def anyadir_desde_fich(self, nf: str) -> None:
        with open(os.path.normpath(nf), "r", encoding="utf-8") as f_r:
            for linea in f_r:
                lista = linea.split(":")
                self.__reemplazos[lista[0].strip()] = lista[1].strip()
                
    
    def aplicar(self, n_e: str, n_s: str) -> None:
        with open(os.path.normpath(n_e), "r", encoding="utf-8") as f_e, open(os.path.normpath(n_s), "w", encoding="utf-8") as f_s:
            for linea in f_e:
                for clave in self.__reemplazos:
                    linea = linea.replace(clave, self.__reemplazos[clave])
                f_s.write(linea)
                
                
def main() -> None:
    clase = Reemplazar()
    clase.anyadir("Guerra", "Pepe")
    clase.anyadir("Parra", "Ana")
    clase.anyadir("caballo", "jamelgo")
    clase.anyadir("ataque", "transporte")

    n_r = input("Introduce el nombre del fichero de reemplazos: ")
    n_e = input("Introduce el nombre del fichero de entrada: ")
    n_s = input("Introduce el nombre del fichero de salida: ")
    
    try:
        clase.anyadir_desde_fich(n_r)
        clase.aplicar(n_e, n_s)
    except OSError as exc:
        print(f"Error: [{exc!r}]")

if __name__ == "__main__":
    main()

