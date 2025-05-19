from p4_pizzeria import Pizzeria, PizzeriaError
from p4_pizzaoferta import PizzaOferta
from p4_pizza import Pizza, PizzaError

class PizzeriaOferta(Pizzeria):
    def __init__(self, ingr_gratis: list[str], *args, **kwargs) -> None:
        self.__ig = {i.lower() for i in ingr_gratis}
        super().__init__(*args, **kwargs)
        
    def get_ingr_gratis(self) -> set[str]:
        return self.__ig
    
    #@override
    def anyadir_pedido(self, nombre: str, lista_ingr: list[str]) -> int:
        found = False
        gratis: list[str] = list()
        for ing in lista_ingr:
            if ing.lower() in self.__ig:
                found = True
                gratis.append(ing)
        
        if found == True:
            p = PizzaOferta(self.__ig, nombre, 0)
            p.anyadir_ingredientes(lista_ingr)
            p.anyadir_ingredientes(gratis)
            ret = self._anyadir_pizza(p)
        else:
            ret = super().anyadir_pedido(nombre, lista_ingr)

        return ret

def anyadir_pedidos(pizzeria: Pizzeria) -> None:
    lista_datos = [
        ("Pepe", ["queso", "anchoa"]),
        ("Lola", ["cebolla", "jamon", "salami"]),
        ("Pepe", ["queso", "jamon", "bacon"]),
        ("Lola", ["nata", "huevo", "pollo", "bacon"]),
    ]
    for (nombre, lstingr) in lista_datos:
        try:
            pizzeria.anyadir_pedido(nombre, lstingr)
        except (PizzaError, PizzeriaError) as exc:
            print(f"Error: [{exc!r}]")


def eliminar_pedidos(pizzeria: Pizzeria) -> None:
    lista_eliminar = [
        ("Pepe", 3),
        ("Pepe", 2),
        ("Lola", 2),
        ("Pepe", 99),
        ("Pepe", 1),
        ("xxx", 4),
        ("Lola", 4),
    ]
    for (nombre, codigo) in lista_eliminar:
        try:
            pizzeria.eliminar_pedido(nombre, codigo)
        except (PizzaError, PizzeriaError) as exc:
            print(f"Error: [{exc!r}]")
        print(pizzeria)


# -----------------------------------
def main() -> None:
    try:
        pizzeria = PizzeriaOferta(["jamon", "queso"], "Pizzeria Luigi")
        anyadir_pedidos(pizzeria)
        print(pizzeria)
        eliminar_pedidos(pizzeria)
    except (PizzaError, PizzeriaError) as exc:
        print(f"Error [{exc!r}]")


# -----------------------------------------------------------------------
if __name__ == "__main__":
    main()

    