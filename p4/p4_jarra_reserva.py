from p3_jarra import Jarra, JarraError

class JarraConReserva(Jarra):
    def __init__(self, capacidad_extra_reserva: int, *args, **kwargs) -> None:
        self.__xtr = Jarra("XtrRsv", capacidad_extra_reserva)
        super().__init__(*args, **kwargs)
    
    #@override
    def _llenar_contenido(self, cantidad: int) -> None:
        super()._llenar_contenido(cantidad)
        
        trasf = self.__xtr.get_capacidad() - self.__xtr.get_contenido()
        
        if (trasf > super().get_contenido()):
            trasf = super().get_contenido()
        super()._vaciar_contenido(trasf)
        self.__xtr._llenar_contenido(trasf)

    
    #@override
    def _vaciar_contenido(self, cantidad) -> None:
        super()._vaciar_contenido(cantidad)
        
        trasf = super().get_capacidad() - super().get_contenido()
        
        if (trasf > self.__xtr.get_contenido()):
            trasf = self.__xtr.get_contenido()
        self.__xtr._vaciar_contenido(trasf)
        super()._llenar_contenido(trasf)      
        
    
    #@override
    def __repr__(self):
        return f"JR({super().__repr__()}, J({self.__xtr.get_ident()}, {self.__xtr.get_capacidad()}, {self.__xtr.get_contenido()}))"
    
def main() -> None:
    try:
        prueba_1()
        prueba_2()
        prueba_3()
    except JarraError as exc:
        print(f"Error [{exc}]")


def prueba_1() -> None:
    jarra_A = JarraConReserva(2, "A", 7)
    jarra_B = JarraConReserva(1, "B", 4)
    prueba_jarras("Prueba-1", jarra_A, jarra_B)


def prueba_2() -> None:
    jarra_A = Jarra("A", 7)
    jarra_B = JarraConReserva(1, "B", 4)
    prueba_jarras("Prueba-2", jarra_A, jarra_B)


def prueba_3() -> None:
    jarra_A = JarraConReserva(2, "A", 7)
    jarra_B = Jarra("B", 4)
    prueba_jarras("Prueba-3", jarra_A, jarra_B)


def prueba_jarras(titulo: str, jarra_A: Jarra, jarra_B: Jarra) -> None:
    print(f"----------------\n{titulo}\n----------------")
    print(f"jarra_A: {jarra_A}")
    print(f"jarra_B: {jarra_B}")

    print("llenar jarra_A")
    jarra_A.llenar()
    print(f"jarra_A: {jarra_A}")
    print(f"jarra_B: {jarra_B}")

    print(f"jarra_A: ident: {jarra_A.get_ident()}")
    print(f"jarra_A: capacidad: {jarra_A.get_capacidad()}")
    print(f"jarra_A: contenido: {jarra_A.get_contenido()}")
    print(f"jarra_B: ident: {jarra_B.get_ident()}")
    print(f"jarra_B: capacidad: {jarra_B.get_capacidad()}")
    print(f"jarra_B: contenido: {jarra_B.get_contenido()}")

    print("llenar jarra_B desde jarra_A")
    jarra_B.llenar_desde(jarra_A)
    print(f"jarra_A: {jarra_A}")
    print(f"jarra_B: {jarra_B}")

    print("vaciar jarra_B")
    jarra_B.vaciar()
    print(f"jarra_A: {jarra_A}")
    print(f"jarra_B: {jarra_B}")

    print("llenar jarra_B desde jarra_A")
    jarra_B.llenar_desde(jarra_A)
    print(f"jarra_A: {jarra_A}")
    print(f"jarra_B: {jarra_B}")


if __name__ == "__main__":
    main()
