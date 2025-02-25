def triangle(n: int) ->None:
    for row in range(1, n + 1):
        print("-" * (n - row), end="")
        print("#" * (row * 2 - 1))
            
                    
def main() -> None:
    n = int(input("Introduzca un número: "))
    
    if (n > 0):
        triangle(n)
    else:
        print("Error")
        

if __name__ == "__main__":
    main()