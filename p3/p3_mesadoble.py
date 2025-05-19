from p3_jarra import Jarra, JarraError

class MesaError(RuntimeError):
    pass

class MesaDoble:
    def __init__(self, ident_1: str, capacidad_1: int, ident_2: str, capacidad_2: int, *args, **kwargs) -> None:
        self.__J1 = Jarra(ident_1, capacidad_1)
        self.__J2 = Jarra(ident_2, capacidad_2)
        super().__init__(*args, **kwargs)
    

    def get_ident(self, jpos: int) -> str:
        if jpos == 1:
            ret = self.__J1.get_ident()
        elif jpos == 2:
            ret = self.__J2.get_ident()
        else:
            raise MesaError("Index out of range")
        
        return ret
    
    def get_capacidad(self, jpos: int) -> int:
        if jpos == 1:
            ret = self.__J1.get_capacidad()
        elif jpos == 2:
            ret = self.__J2.get_capacidad()
        else:
            raise MesaError("Index out of range")
        
        return ret
    
    def get_contenido(self, jpos: int) -> int:
        if jpos == 1:
            ret = self.__J1.get_contenido()
        elif jpos == 2:
            ret = self.__J2.get_contenido()
        else:
            raise MesaError("Index out of range")
        
        return ret
    
    def llenar(self, jpos: int) -> None:
        if jpos == 1:
            self.__J1.llenar()
        elif jpos == 2:
            self.__J2.llenar()
        else:
            raise MesaError("Index out of range")
        
    def vaciar(self, jpos: int) -> None:
        if jpos == 1:
            self.__J1.vaciar()
        elif jpos == 2:
            self.__J2.vaciar()
        else:
            raise MesaError("Index out of range")
    
    def llenar_desde(self, jepos: int) -> None:
        if jepos == 1:
            self.__J2.llenar_desde(self.__J1)
        elif jepos == 2:
            self.__J1.llenar_desde(self.__J2)
        else:
            raise MesaError("Index out of range")

    def __repr__(self) -> str:
        return f"M(J({self.__J1.get_ident()}, {self.__J1.get_capacidad()}, J({self.__J1.get_contenido()}), J({self.__J2.get_ident()}, {self.__J2.get_capacidad()}, {self.__J2.get_contenido()}))"


def main() -> None:
    m = MesaDoble("A", 7, "B", 5)

    print(m)
    m.llenar(2)
    print(m)
    m.llenar_desde(2)
    print(m)
    m.llenar(2)
    print(m)
    m.llenar_desde(2)
    m.vaciar(1)
    print(m)
    m.llenar_desde(2)
    print(m)
    m.llenar(2)
    print(m)
    m.llenar_desde(2)


if __name__ == "__main__":
    main()
    

        

    

    
