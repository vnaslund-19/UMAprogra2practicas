from p3_libro import Libro, LibroError

class LibreriaError(RuntimeError):
    pass

class Libreria:
    def __init__(self, *args, **kwargs) -> None:
        self.__libros: dict[str, dict[str, Libro]] = dict()
        super().__init__(*args, **kwargs)
    
    def anyadir_libro(self, autor: str, titulo: str, precio_base: float) -> None:
        l = Libro(autor, titulo, precio_base)
        self._insertar_libro(l)
    
    def _insertar_libro(self, libro: Libro) -> None:
        autor = libro.get_autor().lower()
        if autor not in self.__libros:
            self.__libros[autor] = dict()
        self.__libros[autor][libro.get_titulo().lower()] = libro
    
    def eliminar_libro(self, autor: str, titulo: str) -> None:
        autor = autor.lower()
        titulo = titulo.lower()

        if autor in self.__libros and titulo in self.__libros[autor]:
            del self.__libros[autor][titulo]
            if len(self.__libros[autor]) == 0:
                del self.__libros[autor]
        else:
            raise LibreriaError(f"Libro no encontrado ({autor}, {titulo})")
    
    def eliminar_autor(self, autor: str) -> None:
        autor = autor.lower()
        
        if autor in self.__libros:
            self.__libros[autor].clear()
            del self.__libros[autor]
        else:
            raise LibreriaError("Autor no encontrado {autor}")
    
    def consultar_cantidad_libros(self) -> int:
        cantidad: int = 0

        for autor in self.__libros:
            cantidad += len(self.__libros[autor])
        
        return cantidad
    
    def consultar_libro(self, autor: str, titulo: str) -> Libro:
        autor = autor.lower()
        titulo = titulo.lower()

        if autor in self.__libros and titulo in self.__libros[autor]:
            ret = self.__libros[autor][titulo]
        else:
            raise LibreriaError(f"Libro no encontrado ({autor}, {titulo})")
        
        return ret
    
    def calc_precio_final(self, autor: str, titulo: str) -> float:
        autor = autor.lower()
        titulo = titulo.lower()

        if autor in self.__libros and titulo in self.__libros[autor]:
            ret = self.__libros[autor][titulo].calc_precio_final()
        else:
            raise LibreriaError(f"Libro no encontrado ({autor}, {titulo})")
        
        return ret
    
    def __repr__(self) -> str:
        libl: list[Libro] = list()
        for autor in self.__libros:
            libl.extend(self.__libros[autor].values())
        return str(libl)
    

def anyadir_libros(libreria: Libreria) -> None:
    libros = [
        ("george orwell", "1984", 8.20),
        ("Philip K. Dick", "¿Sueñan los androides con ovejas eléctricas?", 3.50),
        ("Isaac Asimov", "Fundación e Imperio", 9.40),
        ("Ray Bradbury", "Fahrenheit 451", 7.40),
        ("Aldous Huxley", "Un Mundo Feliz", 6.50),
        ("xxx", "xxx", -1.00),
        ("Isaac Asimov", "La Fundación", 7.30),
        ("William Gibson", "Neuromante", 8.30),
        ("Isaac Asimov", "Segunda Fundación", 8.10),
        ("Isaac Newton", "arithmetica universalis", 7.50),
        ("George Orwell", "1984", 6.20),
        ("Isaac Newton", "Arithmetica Universalis", 10.50)
    ]
    for (autor, titulo, precio) in libros:
        try:
            libreria.anyadir_libro(autor, titulo, precio)
        except (LibroError, LibreriaError) as exc:
            print(f"Error: {exc!r}")

def eliminar_libros(libreria: Libreria) -> None:
    eliminar = [
        ("George Orwell", "1984"),
        ("Aldous Huxley", "Un Mundo Feliz"),
        ("xxx", "xxx"),
        ("Isaac Newton", "Arithmetica Universalis"),
        ("Isaac Asimov", "La Fundación")
    ]
    for (autor, titulo) in eliminar:
        try:
            libreria.eliminar_libro(autor, titulo)
        except LibreriaError as exc:
            print(f"Error: {exc!r}")

def mostrar_precios(libreria: Libreria) -> None:
    precios = [
        ("Philip K. Dick", "¿Sueñan los androides con ovejas eléctricas?"),
        ("isaac asimov", "fundación e imperio"),
        ("Isaac Asimov", "Segunda Fundación"),
        ("Isaac Newton", "Arithmetica Universalis"),
        ("Ray Bradbury", "Fahrenheit 451"),
        ("william gibson", "neuromante")
    ]
    for (autor, titulo) in precios:
        try:
            print(f"PrecioFinal({autor}, {titulo}):", round(libreria.calc_precio_final(autor, titulo), 2))
        except LibreriaError as exc:
            print(f"Error: {exc!r}")

def eliminar_autores(libreria: Libreria) -> None:
    autores = [
        "Isaac Asimov",
        "xxx"
    ]
    for autor in autores:
        try:
            libreria.eliminar_autor(autor)
        except LibreriaError as exc:
            print(f"Error: {exc!r}")

def main() -> None:
    try:
        libreria = Libreria()
        anyadir_libros(libreria)

        print()
        print("Cantidad de libros almacenados:", libreria.consultar_cantidad_libros())
        print()
        print(libreria)
        print()

        eliminar_libros(libreria)

        print()
        print("Cantidad de libros almacenados:", libreria.consultar_cantidad_libros())
        print()
        print(libreria)
        print()

        mostrar_precios(libreria)
        print()

        eliminar_autores(libreria)
        print()
        print(libreria)
        print()

    except LibreriaError as exc:
        print(f"Error [{exc}]")

if __name__ == "__main__":
    main()




                

    
