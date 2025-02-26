def mcd(num1: int, num2: int) ->int:
    if num1 < 0:
        num1 *= -1
    
    if num2 < 0:
        num2 *= -1
        
    if num1 == 0:
        res = num2
    elif num2 == 0:
        res = num1
    else:
        while num1 != num2:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
        res = num1
    
    return res
    
        
    
def son_coprimos(num1: int, num2: int) -> bool:
    return mcd(num1, num2) == 1

def print_coprimos(l: int, u: int) -> None:
    for i in range(l, u+1):
        for j in range(i+1, u+1):
            if son_coprimos(i, j):
                print(f"Coprimos: {i} {j}")

def main() -> None:
    l = int(input("Introduce el número menor del intervalo: "))
    u = int(input("Introduce el número mayor del intervalo: "))

    if (u > l and l > 0):
        print_coprimos(l, u)
    else:
        print("Error")


if __name__ == "__main__":
    main()