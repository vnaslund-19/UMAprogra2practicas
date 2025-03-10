def mostrar(med: float, max: int, min: int) -> None:
    print(f"Mayor: {max}")
    print(f"Menor: {min}")
    print(f"Media: {med:.2f}")

def main() -> None:
    str = input("Introduzca una secuencia de números (separados por espacios) hasta línea vacía: ")
    
    
    sum: int = 0
    count: int = 0
    max: int = -1
    min: int = -1
    while not str == "":
        nums = str.split()
        for word in nums:
            num = int(word)
            if max == -1 or num > max:
                max = num
            if min == -1 or num < min:
                min = num
            sum += num
            count += 1
        str = input()
    
    if (count == 0):
        print("Error")
    else:
        mostrar(sum/count, max, min)

if __name__ == "__main__":
    main()
    
            