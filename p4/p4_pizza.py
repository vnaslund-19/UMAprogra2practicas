from typing import Final
import functools

PRECIO_FIJO: Final = 5.5
PRECIO_INGREDIENTE: Final = 1.5

class PizzaError(RuntimeError):
    pass

@functools.total_ordering
class Pizza:
    def __init__(self, nombre: str, codigo: int, *args, **kwargs) -> None:
        self.__nom = nombre
        self.__cod = codigo
        self.__ing: list[str] = list()
        super().__init__(*args, **kwargs)
        
    def set_codigo(self, codigo: int) -> None:
        if self.__cod == 0:
            self.__cod = codigo
        else:
            raise PizzaError("Codigo ya existe")
    
    def anyadir_ingredientes(self, lista_ingr: list[str]) -> None:
        self.__ing.extend(lista_ingr)
    
    def get_nombre(self) -> str:
        return self.__nom
    
    def get_codigo(self) -> int:
        return self.__cod
    
    def get_ingredientes(self) -> list[str]:
        return self.__ing
    
    def calc_precio(self) -> float:
        return PRECIO_FIJO + len(self.__ing) * PRECIO_INGREDIENTE
    
    def __repr__(self) -> str:
        return f"Pz({self.__nom}, {self.__cod}, {self.__ing}, {round(self.calc_precio(), 2)})"
    
    def _atrib_comp(self) -> tuple:
        return(self.__nom.lower(), self.__cod)
    
    def __hash__(self) -> int:
        return hash(self._atrib_comp())
    
    def __eq__(self, other: object) -> bool:
        if self is other:
            ok = True
        elif isinstance(other, Pizza):
            ok = self._atrib_comp() == other._atrib_comp()
        else:
            ok = NotImplemented
        return ok

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Pizza):
            ok = self._atrib_comp() < other._atrib_comp()
        else:
            ok = NotImplemented
        return ok
    