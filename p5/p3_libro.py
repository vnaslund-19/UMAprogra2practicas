
import functools

class LibroError(RuntimeError):
    """Errores en el procesamiento de los datos de la práctica"""
    pass


@functools.total_ordering
class Libro:
    """Libro con autor, título y precio"""
    
    def __init__(self, autor: str, titulo: str, precio_base: float, *args, **kwargs) -> None:
        if precio_base < 0:
            raise LibroError("Precio base negativo")
        self.__autor = autor
        self.__titulo = titulo
        self.__precio_base = precio_base
        self.__iva = 10.0
        super().__init__(*args, **kwargs)

    def get_autor(self) -> str:
        return self.__autor
    
    def get_titulo(self) -> str:
        return self.__titulo
    
    def get_precio_base(self) -> float:
        return self.__precio_base
    
    def get_iva(self) -> float:
        return self.__iva

    def set_iva(self, iva: float) -> None:
        if iva < 0:
            raise LibroError("Iva negativo")
        self.__iva = iva
    
    def _calc_base_imponible(self) -> float:
        return self.__precio_base

    def calc_precio_final(self) -> float:
        return self._calc_base_imponible() + self._calc_base_imponible() * self.get_iva() / 100.0
    
    # @override
    def __repr__(self) -> str:
        return (f"({self.__autor}; {self.__titulo}; {round(self.__precio_base, 2)};"
                f" {round(self.__iva, 2)}%; {round(self.calc_precio_final(), 2)})")

    def _atrib_comp(self) -> tuple:
        return (self.__autor.lower(), self.__titulo.lower())

    # @override
    def __hash__(self) -> int:
        return hash(self._atrib_comp())
    
    # @override
    def __eq__(self, other: object) -> bool:
        if self is other:
            ok = True
        elif isinstance(other, Libro):
            ok = (self._atrib_comp() == other._atrib_comp())
        else:
            ok = NotImplemented
        return ok
    
    # @override
    def __lt__(self, other: object) -> bool:
        if isinstance(other, Libro):
            ok = (self._atrib_comp() < other._atrib_comp())
        else:
            ok = NotImplemented
        return ok

#-----------------------------------------------------------------------
def crear_libros() -> list[Libro]:
    datos = [ ("George Orwell", "1984", 6.20),
              ("xxx", "xxx", -1.00),
              ("Ray Bradbury", "Fahrenheit 451", 7.40) ]
    libros: list[Libro] = list()
    for (autor, titulo, precio) in datos:
        try:
            libros.append( Libro(autor, titulo, precio) )
        except LibroError as exc:
            print(f"Error: {exc!r}")
    return libros
#-----------------------------------------------------------------------
def mostrar_libros(libros: list[Libro]) -> None:
    print()
    for libro in libros:
        print(libro)
#-----------------------------------------------------------------------
def cambiar_iva(libros: list[Libro], iva: float) -> None:
    for libro in libros:
        try:
            libro.set_iva(iva)
        except LibroError as exc:
            print(f"Error: {exc!r}")
#-----------------------------------------------------------------------
def main() -> None:
    try:
        libros = crear_libros()
        mostrar_libros(libros)
        cambiar_iva(libros, 20.0)
        mostrar_libros(libros)
    except LibroError as exc:
        print(f"Error [{exc}]")

if __name__ == "__main__":
    main()

