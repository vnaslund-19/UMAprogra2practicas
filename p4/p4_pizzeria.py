from p4_pizza import Pizza, PizzaError

class PizzeriaError(RuntimeError):
    pass


class Pizzeria:
    def __init__(self, nombre: str, *args, **kwargs) -> None:
        self.__nombre = nombre
        self.__cnt_pedidos = 0
        self.__pedidos: dict[str,list[Pizza]] = dict()
        super().__init__(*args, **kwargs)
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_cnt_pedidos(self) -> int:
        return self.__cnt_pedidos
    
    def get_pedidos(self) -> dict[str,list[Pizza]]:
        return self.__pedidos
    
    def anyadir_pedido(self, nombre: str, lista_ingr: list[str]) -> int:
        p = Pizza(nombre, 0)
        p.anyadir_ingredientes(lista_ingr)
        return self._anyadir_pizza(p)
        
    
    def _anyadir_pizza(self, pizza: Pizza) -> int:
        self.__cnt_pedidos += 1
        pizza.set_codigo(self.__cnt_pedidos)
        nom = pizza.get_nombre().lower()
        if nom not in self.__pedidos:
            self.__pedidos[nom] = list()
        self.__pedidos[nom].append(pizza)
        
        return self.__cnt_pedidos
    
    def eliminar_pedido(self, nombre: str, codigo: int) -> None:
        found = False
        nom = nombre.lower()
        if nom in self.__pedidos:
            for p in self.__pedidos[nom]:
                if p.get_codigo() == codigo:
                    self.__pedidos[nom].remove(p)
                    found = True
                    if len(self.__pedidos[nom]) == 0:
                        del self.__pedidos[nom]
        if not found:
            raise PizzeriaError("Pedido no existe")
    
    
    def eliminar_pedidos_por_codigo(self, lista_cods: list[int]) -> list[Pizza]:
        elim: list[Pizza] = list()
        noms: list[str] = list()
        for num in lista_cods:
            for cli in self.__pedidos:
                for p in self.__pedidos[cli]:
                    if p.get_codigo() == num:
                        self.__pedidos[cli].remove(p)
                        elim.append(p)
                        if len(self.__pedidos[cli]) == 0:
                            noms.append(cli)
        for nom in noms:
            del self.__pedidos[nom]
        return elim
    
    def __repr__(self) -> str:
        return f"Pr({self.__nombre}, {self.__cnt_pedidos}, {self.__pedidos})"
    
def main() -> None:
    p = Pizzeria("Pizzeria Luigi")

    p.anyadir_pedido("Pepe", ["queso", "anchoa"])
    p.anyadir_pedido("Lola", ["cebolla", "jamon", "salami"])
    p.anyadir_pedido("Pepe", ["queso", "jamon", "bacon"])
    p.anyadir_pedido("Lola", ["nata", "huevo", "pollo", "bacon"])
    print(p)

    try:
        p.eliminar_pedido("Pepe", 3)
    except PizzeriaError as exc:
        print(f"Error: [{exc!r}]")
    print(p)
    
    try:
        p.eliminar_pedido("Pepe", 2)
    except PizzeriaError as exc:
        print(f"Error: [{exc!r}]")
    print(p) 

    try:
        p.eliminar_pedido("Lola", 2)
    except PizzeriaError as exc:
        print(f"Error: [{exc!r}]")
    print(p)

    try:
        p.eliminar_pedido("Pepe", 99)
    except PizzeriaError as exc:
        print(f"Error: [{exc!r}]")
    print(p)

    try:
        p.eliminar_pedido("Pepe", 1)
    except PizzeriaError as exc:
        print(f"Error: [{exc!r}]")
    print(p)

    try:
        p.eliminar_pedido("xxx", 4)
    except PizzeriaError as exc:
        print(f"Error: [{exc!r}]")
    print(p)

    try:
        p.eliminar_pedido("Lola", 4)
    except PizzeriaError as exc:
        print(f"Error: [{exc!r}]")
    print(p)
if __name__ == "__main__":
    main()
        
        

                        
                    
        