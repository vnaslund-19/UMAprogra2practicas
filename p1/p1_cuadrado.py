def square(n: int) ->None:
    for row in range(n):
        if (row == 0 or row == n - 1):
            print("#" * n)
        else:
            for col in range(n):
                if (col == 0
                    or row == col
                    or row == n - col - 1):
                    print("#", end = "")
                elif (col == n-1):
                    print("#")
                else:
                    print("-", end = "")
                    
def main() -> None:
    n = int(input("Introduzca un número: "))
    
    if (n > 0):
        square(n)
    else:
        print("Error")
        

if __name__ == "__main__":
    main()