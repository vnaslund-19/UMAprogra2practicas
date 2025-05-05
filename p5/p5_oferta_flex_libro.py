from p3_libro import Libro, LibroError
#from p4_libro_oferta import LibroOferta
from abc import ABC, abstractmethod

class OfertaFlexAbstracta(ABC):
    @abstractmethod
    def get_descuento(self, libro: Libro) -> float:
        pass

class OfertaPrecio(OfertaFlexAbstracta):
    def __init__(self, porc_descuento: float, umbral_precio: float, *args, **kwargs) -> None:
        if porc_descuento < 0:
            raise LibroError("Porcentaje de descuento negativo")
        else:
            self.__porc_descuento = porc_descuento
            self.__umbral_precio = umbral_precio
            super().__init__(*args, **kwargs)
    
    # @override
    def get_descuento(self, libro: Libro) -> float:
        desc = 0.0
        if libro.get_precio_base() >= self.__umbral_precio:
            desc = self.__porc_descuento
        return desc
    
    # @override
    def __repr__(self) -> str:
        return f"{round(self.__porc_descuento, 2)}%({round(self.__umbral_precio, 2)})"
    
class OfertaAutor(OfertaFlexAbstracta):
    def __init__(self, porc_descuento: float, autores_oferta: list[str], *args, **kwargs) -> None:
        if porc_descuento < 0:
            raise LibroError("Porcentaje de descuento negativo")
        else:
            self.__porc_descuento = porc_descuento
            self.__autores_oferta = {autor.lower() for autor in autores_oferta}
            super().__init__(*args, **kwargs)
    
    # @override
    def get_descuento(self, libro: Libro) -> float:
        desc = 0.0
        if libro.get_autor().lower() in self.__autores_oferta:
            desc = self.__porc_descuento
        return desc
    
    # @override
    def __repr__(self) -> str:
        return f"{round(self.__porc_descuento, 2)}%{self.__autores_oferta}" 

def main() -> None:
    try:
        l1 = Libro("George Orwell", "1984", 6.20)
        print(f"Libro: {l1}")
        op1 = OfertaPrecio(20.0, 5.5)
        print(f"Oferta-Precio: {op1.get_descuento(l1)}")
        oa1 = OfertaAutor(10.0, ["george orwell", "isaac asimov"])
        print(f"Oferta-Autor: {oa1.get_descuento(l1)}")
    except LibroError as exc:
        print(f"Error: {exc!r}")
        
        
if __name__ == "__main__":
    main()