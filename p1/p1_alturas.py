from math import sqrt

def procesar(l: list[float], n: int) -> None:
    sum: float = 0
    max = min = l[0]
    
    for elem in l:
        if elem > max:
            max = elem
        elif elem < min:
            min = elem
        sum += elem
    media = sum / n
    
    sum = 0
    baj: int = 0
    alt: int = 0
    for elem in l:
        if elem < media:
            baj += 1
        elif elem > media:
            alt += 1
        sum += (elem - media)**2
    des: float = sqrt(sum / n)

    print(f"Mayor: {max:.2f}")
    print(f"Menor: {min:.2f}")
    print(f"Media: {media:.2f}")
    print(f"DesTip: {des:.2f}")
    print(f"cntBajos: {baj}")
    print(f"cntAltos: {alt}")
    
    
def main() -> None:
    line = input("Introduzca una secuencia de alturas (separados por espacios) hasta línea vacía: ")
    l: list[float] = list()
    
    while not line == "":
        nums = line.split()
        for word in nums:
            num = float(word)
            l.append(num)
        line = input()
    
    n = len(l)
    if n == 0:
        print("Error")
    else:
        procesar(l, n)
        
        


if __name__ == "__main__":
    main()