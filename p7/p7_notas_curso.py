import csv
import os.path 

class CalcNotasCurso:
    def __init__(self, *args, **kwargs) -> None:
        self.__filas: list[list] = list()
        super().__init__(*args, **kwargs)
    
    def cargar_fichero_csv(self, nombre_fich: str) -> None:
        self.__filas.clear()
        with open(os.path.normpath(nombre_fich), "r", newline="", encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            for fila in csv_reader:
                self.__filas.append(fila)
    
    def calcular_notas(self) -> None:
        #dict =  {"ExamFinal": 4, "Controles": [1,2,3]}
        
        if len(self.__filas) > 0:
            self.__filas[0].append("NotaFinal")
            self.__filas[0].append("Calificación")
        
            for fila in self.__filas[1:]:
                nota: float = (((fila[1] + fila[2] + fila[3]) / 3) * 0.4) + (fila[4] * 0.6)
                nota = round(nota, 1)
                fila.append(nota)
                if nota < 5:
                    cal = "Suspenso"
                elif nota < 7:
                    cal = "Aprobado"
                elif nota < 9:
                    cal = "Notable"
                elif nota < 9.5:
                    cal = "Sobresaliente"
                elif nota <= 10:
                    cal = "Sobresal-MH"
                else:
                    cal = "ERROR"
                fila.append(cal)
            
    
    def guardar_fichero_csv(self, nombre_fich: str) -> None:
        with open(os.path.normpath(nombre_fich), "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerows(self.__filas)
    
    def __repr__(self) -> str:
        return f"{self.__filas}"

def main() -> None:
    f_e = input("Introduce el nombre del fichero CSV de entrada: ")
    f_s = input("Introduce el nombre del fichero CSV de salida: ")
    
    Notas = CalcNotasCurso()
    Notas.cargar_fichero_csv(f_e)
    Notas.calcular_notas()
    Notas.guardar_fichero_csv(f_s)
    print(Notas)
    

if __name__ == "__main__":
    main()
