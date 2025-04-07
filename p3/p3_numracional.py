from math import gcd
from functools import total_ordering

class RacionalError(RuntimeError):
    pass

@total_ordering
class NumeroRacional:
    def __init__(self, num: int, den: int, *args, **kwargs) -> None:
        if not isinstance(num, int):
            raise RacionalError("Num no es int")
        if not isinstance(den, int):
            raise RacionalError("Den no es int")
        if den == 0:
            raise RacionalError("Error de division por 0")
        
        self.__num = num
        self.__den = den
        super().__init__(*args, **kwargs)
        self.__normalizar()
        
    def get_numerador(self) -> int:
        return self.__num

    def get_denominador(self) -> int:
        return self.__den
    
    def sumar(self, num: 'NumeroRacional') -> 'NumeroRacional':
        num1 = self.__num * num.get_denominador()
        num2 = num.get_numerador() * self.__den
        new_den = self.__den * num.get_denominador()
        
        return NumeroRacional(num1 + num2, new_den)
    
    def restar(self, num: 'NumeroRacional') -> 'NumeroRacional':
        num1 = self.__num * num.get_denominador()
        num2 = num.get_numerador() * self.__den
        new_den = self.__den * num.get_denominador()
        
        return NumeroRacional(num1 - num2, new_den)
    
    def multiplicar(self, num: 'NumeroRacional') -> 'NumeroRacional':
        new_num = self.__num * num.get_numerador()
        new_den = self.__den * num.get_denominador()
        
        return NumeroRacional(new_num, new_den)
    
    def dividir(self, num: 'NumeroRacional') -> 'NumeroRacional':
        if (num.get_numerador() == 0):
            raise RacionalError("Error de division por 0")
        new_num = self.__num * num.get_denominador() # dar la vuelta a num para convertir division en multiplicacion
        new_den = self.__den * num.get_numerador()
        
        return NumeroRacional(new_num, new_den)
    
    def __repr__(self) -> str:
        if self.__den == 1:
            res = f"{self.__num}"
        else:
            res = f"{self.__num}/{self.__den}"
        return res
    
    def _atrib_comp(self) -> tuple:
        return (self.__num, self.__den)
    
    def __eq__(self, other: object) -> bool:
        if self is other:
            ok = True
        elif isinstance(other, NumeroRacional):
            ok = (self._atrib_comp() == other._atrib_comp())
        else:
            ok = NotImplemented
        return ok
    
    def __lt__(self, other: object) -> bool:
        if isinstance(other, NumeroRacional):
            ok = self.__num * other.get_denominador() < other.get_numerador() * self.__den
        else:
            ok = NotImplemented
        return ok
    
    def __hash__(self) -> int:
        return hash(self._atrib_comp())
    
    def __normalizar(self):
        if self.__num == 0:
            self.__den = 1
        else:
            divisor = abs(gcd(self.__num, self.__den))
            self.__num //= divisor # IMP: div entera (//), si / devuelve un float con .0
            self.__den //= divisor
            
            if self.__den < 0:
                self.__den *= -1
                self.__num *= -1

def main():
    try:
        # Leer primera fracción
        num1 = int(input("Introduce numerador: "))
        den1 = int(input("Introduce denominador: "))
        r1 = NumeroRacional(num1, den1)
        print(f"R1: {r1}")

        # Leer segunda fracción
        num2 = int(input("Introduce numerador: "))
        den2 = int(input("Introduce denominador: "))
        r2 = NumeroRacional(num2, den2)
        print(f"R2: {r2}")

        # Operaciones
        r3 = r1.sumar(r2)
        print(f"R3 (r1 + r2): {r3}")

        r4 = r3.restar(r2)
        print(f"R4 (r3 - r2): {r4}")

        r5 = r3.restar(r1)
        print(f"R5 (r3 - r1): {r5}")

        r6 = r1.multiplicar(r2)
        print(f"R6 (r1 * r2): {r6}")

        r7 = r6.dividir(r2)
        print(f"R7 (r6 / r2): {r7}")

        r8 = r6.dividir(r1)
        print(f"R8 (r6 / r1): {r8}")

    except RacionalError as err:
        print(f"ERROR: {err}")

                
if __name__ == "__main__":
    main()

    

    

    