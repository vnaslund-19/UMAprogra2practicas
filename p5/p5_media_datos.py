from abc import ABC, abstractmethod
from p5_datos import Datos

class MediaError(RuntimeError):
    pass

class CalculoMediaAbstracto(ABC):
    @abstractmethod
    def calc_media(self, lista_nums: list[int|float]) -> float:
        pass
    

class MediaAritmetica(CalculoMediaAbstracto):
    # @override
    def calc_media(self, lista_nums: list[int|float]) -> float:
        l = len(lista_nums)
        if l == 0:
            raise MediaError("Lista vacía")
        else:
            return sum(lista_nums) / l
    
class MediaArmonica(CalculoMediaAbstracto):
    # @override
    def calc_media(self, lista_nums: list[int|float]) -> float:
        k = 0
        suma = 0.0
        for x in lista_nums:
            if (x > 0):
                suma += (1 / x)
                k += 1
        if k == 0:
            raise MediaError("No hay datos válidos")
        return (k / suma)

class MediaTruncada(CalculoMediaAbstracto):
    def __init__(self, valor_min: float, valor_max: float, *args, **kwargs) -> None:
        self.__min = valor_min
        self.__max = valor_max
        super().__init__(*args, **kwargs)
    
    def calc_media(self, lista_nums: list[int|float]) -> float:
        l = 0
        s = 0.0
        for num in lista_nums:
            if num >= self.__min and num <= self.__max:
                s += num
                l += 1
        if l == 0:
            raise MediaError("No hay datos válidos")
        else:
            return s/l

def main() -> None:
    try:
        d = Datos()
        d.anyadir_datos([62, 66, 52, 54, 52, 56, 67, 61, 68, 55, 66, 64, 69, 60, 54, 51, 57, 65, 56, 51])
        d.anyadir_datos([35, 78, 45, 67])
        d.eliminar_datos([83, 23, 54, 67, 64])
        print(f"Datos: {d}")
        
        calculadoras: list[CalculoMediaAbstracto] = [
            MediaAritmetica(),
            MediaArmonica(),
            MediaTruncada(55.0, 65.0),
        ]
    #-------------------------------
        for calc in calculadoras:
            print(f"{type(calc).__name__}: {round(d.calc_media(calc), 2)}")
#-------------------------------
    except MediaError as exc:
        print(f"Error [{exc}]")

if __name__ == "__main__":
    main()
        
        
                    
        
