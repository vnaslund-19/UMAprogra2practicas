
class JarraError(RuntimeError):
    pass

class Jarra:
    def __init__(self, ident: str, capacidad: int, *args, **kwargs):
        if capacidad > 0:
            self.__ident: str = ident
            self.__capacidad: int = capacidad
            self.__contenido: int = 0
        else:
            raise JarraError("Capacidad <= 0")
        super().__init__(*args, **kwargs)
    
    def get_ident(self) -> str:
        return self.__ident
    
    def get_capacidad(self) -> int:
        return self.__capacidad
    
    def get_contenido(self) -> int:
        return self.__contenido
    
    def _llenar_contenido(self, cantidad: int) -> None:
        if cantidad < 0:
            raise JarraError("cantidad < 0")
        elif cantidad + self.__contenido > self.__capacidad:
            raise JarraError("Overflow")
        else:
            self.__contenido += cantidad
    
    def _vaciar_contenido(self, cantidad: int) -> None:
        if cantidad < 0:
            raise JarraError("cantidad < 0")
        elif cantidad > self.__contenido:
            raise JarraError("Underflow")
        else:
            self.__contenido -= cantidad
    
    def llenar(self) -> None:
        self._llenar_contenido(self.__capacidad - self.__contenido)
    
    def vaciar(self) -> None:
        self._vaciar_contenido(self.__contenido)
    
    def llenar_desde(self, otra_jarra: 'Jarra') -> None:
        if otra_jarra is self:
            raise JarraError("Same same")
        
        cantidad = otra_jarra.get_contenido()

        if cantidad + self.__contenido > self.__capacidad:
            cantidad = self.__capacidad - self.__contenido
        
        self._llenar_contenido(cantidad)
        otra_jarra._vaciar_contenido(cantidad)
    
    def __repr__(self) -> str:
        return f"J({self.__ident}, {self.__capacidad}, {self.__contenido})"
        
def main() -> None:
    jarra_A = Jarra("A", 7)
    jarra_B = Jarra("B", 4)
    print(f"{jarra_A}, {jarra_B}")

    jarra_A.llenar()
    print("llenar jarra_A")
    print(f"{jarra_A}, {jarra_B}")

    print(f"jarra_A: ident: {jarra_A.get_ident()}")
    print(f"jarra_A: capacidad: {jarra_A.get_capacidad()}")
    print(f"jarra_A: contenido: {jarra_A.get_contenido()}")

    print(f"jarra_B: ident: {jarra_B.get_ident()}")
    print(f"jarra_B: capacidad: {jarra_B.get_capacidad()}")
    print(f"jarra_B: contenido: {jarra_B.get_contenido()}")

    print("llenar jarra_B desde jarra_A")
    jarra_B.llenar_desde(jarra_A)
    print(f"{jarra_A}, {jarra_B}")

    print("vaciar jarra_B")
    jarra_B.vaciar()
    print(f"{jarra_A}, {jarra_B}")

    print("llenar jarra_B desde jarra_A")
    jarra_B.llenar_desde(jarra_A)
    print(f"{jarra_A}, {jarra_B}")





if __name__ == "__main__":
    main()