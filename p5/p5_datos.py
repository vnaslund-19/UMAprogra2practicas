from abc import ABC, abstractmethod
from typing import Protocol

class PrtclCaluloMedia(Protocol):
    def calc_media(self, lista_nums: list[int|float]) -> float:
        pass

class Datos:
    def __init__(self, *args, **kwargs) -> None:
        self.__lista_nums: list[int|float] = list()
        super().__init__(*args, **kwargs)
    
    def get_datos(self) -> list[int|float]:
        return self.__lista_nums
    
    def anyadir_datos(self, lista_nums: list[int|float]) -> None:
        self.__lista_nums.extend(lista_nums)
    
    def eliminar_datos(self, lista_nums: list[int|float]) -> None:
        for e in lista_nums:
            if e in self.__lista_nums:
                self.__lista_nums.remove(e)
    
    def calc_media(self, calculadora: PrtclCaluloMedia) -> float:
        return calculadora.calc_media(self.__lista_nums)
    
    def __repr__(self) -> str:
        return f"{self.__lista_nums}"
    
def main() -> None:
    try:
    #-------------------------------
        datos = Datos()
        datos.anyadir_datos([62, 66, 52, 54, 52, 56, 67, 61, 68, 55, 66, 64, 69, 60, 54, 51, 57, 65, 56, 51])
        datos.anyadir_datos([35, 78, 45, 67])
        datos.eliminar_datos([83, 23, 54, 67, 64])
        #-------------------------------
        print(f"Datos: {datos}")
        #-------------------------------
    except ValueError as exc:
        print(f"Error [{exc}]")
    #-----------------------------------------------------------------------

if __name__ == "__main__":
    main()



