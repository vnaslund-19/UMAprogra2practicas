from p3_libro import Libro, LibroError

class LibroOferta(Libro):
    def __init__(self, porc_descuento: float, *args, **kwargs) -> None:
        if porc_descuento < 0:
            raise LibroError("Porcentaje de descuento negativo")
        else:
            self.__porc_descuento = porc_descuento
            super().__init__(*args, **kwargs)
        
    
    def get_descuento(self) -> float:
        return self.__porc_descuento
    
    def set_descuento(self, porc_descuento: float) -> None:
        if porc_descuento < 0:
            raise LibroError("Porcentaje de descuento negativo")
        else:
            self.__porc_descuento = porc_descuento

    # @override
    def _calc_base_imponible(self) -> float:
        return self.get_precio_base() - self.get_precio_base() * self.__porc_descuento / 100
    
    # @override
    def __repr__(self) -> str:
        return f"({self.get_autor()}; {self.get_titulo()}; {round(self.get_precio_base(), 2)}; {self.get_descuento()}%; {round(self._calc_base_imponible(), 2)}; {self.get_iva()}%; {round(self.calc_precio_final(), 2)})"
    

def main() -> None:
    try:
        l1 = LibroOferta(7.5, "George Orwell", "1984", 6.20)
    except LibroError as exc:
        print(f"Error [{exc!r}]")
    
    try:
        l2 = LibroOferta(5.00, "xxx", "xxx", -1.00)
    except LibroError as exc:
        print(f"Error [{exc!r}]")
    
    try:
        l3 = LibroOferta(-5.00, "xxx", "xxx", 20.00)
    except LibroError as exc:
        print(f"Error [{exc!r}]")
    
    try:
        l4 = LibroOferta(8.5, "Ray Bradbury", "Fahrenheit 451", 7.40)
    except LibroError as exc:
        print(f"Error [{exc!r}]")
    
    # MIRAR SOLUCION, como imprime solo los sin errores?
    print(l1)
    print(l4)
    
    l1.set_iva(20.0)
    l4.set_iva(20.0)
    
    print()
    print(l1)
    print(l4)
    
    
    
if __name__ == "__main__":
    main()
    
    
