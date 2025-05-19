from p4_pizza import Pizza, PizzaError
from typing import Final
import functools

PRECIO_FIJO: Final = 5.5
PRECIO_INGREDIENTE: Final = 1.5

class PizzaOferta(Pizza):
    def __init__(self, ingr_gratis: (list[str]|set[str]), *args, **kwargs) -> None:
        self.__ingr_gratis = {i.lower() for i in ingr_gratis}
        super().__init__(*args, **kwargs)
        
    def get_ingr_gratis(self) -> set[str]:
        return self.__ingr_gratis
    
    def calc_precio(self) -> float:
        ing_no_gratis = 0
        for ing in self.get_ingredientes():
            if ing.lower() not in self.__ingr_gratis:
                ing_no_gratis += 1
        return PRECIO_FIJO + ing_no_gratis * PRECIO_INGREDIENTE