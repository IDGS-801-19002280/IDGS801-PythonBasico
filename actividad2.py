class Calculadora:
    
    def suma(self, num1, num2) -> str:
        return "La suma es: {}".format(num1 + num2)
    
    def resta(self, num1, num2) -> str:
        return "La resta es: {}".format(num1 - num2)
    
    def multiplicacion(self, num1, num2) -> str:
        return "La multiplicacion es: {}".format(num1 * num2)
    
    def division(self, num1, num2) -> str:
        return "La división es: {}".format(num1 / num2)

def main():
    calc = Calculadora()
    opt = -1
    
    while opt != 0:
        print("---------- CALCULADORA ----------\nSeleccione una opcion:\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n0.-Salir")
        opt = int(input('Operación: '))
        match opt:
            case 1:
                num1 = int(input('Numero 1: '))
                num2 = int(input('Numero 2: '))
                print(calc.suma(num1, num2))
            case 2:
                num1 = int(input('Numero 1: '))
                num2 = int(input('Numero 2: '))
                print(calc.resta(num1, num2))
            case 3:
                num1 = int(input('Numero 1: '))
                num2 = int(input('Numero 2: '))
                print(calc.multiplicacion(num1, num2))
            case 4:
                num1 = int(input('Numero 1: '))
                num2 = int(input('Numero 2: '))
                print(calc.division(num1, num2))
            case 0:
                print("Salir!")
                break
            case _:
                print("Invalido")

if __name__ == '_main_':
    main()