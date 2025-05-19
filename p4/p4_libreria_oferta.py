from p3_libro import Libro, LibroError
from p3_libreria import Libreria, LibreriaError
from p4_libro_oferta import LibroOferta

class LibreriaOferta(Libreria):
    def __init__(self, porc_descuento: float, autores_oferta: list[str], *args, **kwargs) -> None:
        if porc_descuento < 0:
            raise LibreriaError("Porcentaje de descuento negativo")
        else:
            self.__porc_descuento = porc_descuento
            self.__autores_oferta = {a.lower() for a in autores_oferta}
            super().__init__(*args, **kwargs)
    
    def set_oferta(self, porc_descuento: float, autores_oferta: list[str]) -> None:
        if porc_descuento < 0:
            raise LibreriaError("Porcentaje de descuento negativo")
        else:
            self.__porc_descuento = porc_descuento
            self.__autores_oferta = {a.lower() for a in autores_oferta}
    
    def get_porc_descuento(self) -> float:
        return self.__porc_descuento
    
    def get_autores_oferta(self) -> set[str]:
        return self.__autores_oferta
    
    # @override
    def anyadir_libro(self, autor: str, titulo: str, precio_base: float) -> None:
        if autor.lower() in self.__autores_oferta:
            l = LibroOferta(self.__porc_descuento, autor, titulo, precio_base)
            self._insertar_libro(l)
        else:
            super().anyadir_libro(autor, titulo, precio_base)
    
    def __repr__(self) -> str:
        oferta = f"{round(self.__porc_descuento, 2)}%{self.__autores_oferta}"
        return f"({oferta}, {super().__repr__()})"


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
            print(f"PrecioFinal({autor}, {titulo}):",
                  round(libreria.calc_precio_final(autor, titulo), 2))
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
        autores_oferta = ["George Orwell", "Isaac Asimov"]
        libreria = LibreriaOferta(20.0, autores_oferta)

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
        print(f"Error: {exc!r}")


if __name__ == "__main__":
    main()

