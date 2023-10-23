print("*** Calculadora Basica ***")
print(" ")
print("Ingresa el primer numero")
num1 = int(input())
print("Ingresa el segundo numero")
num2 = int(input())
print("Ingresa la operacion que deseas realizar")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
operacion = int(input())

if operacion == 1:
    resultado = num1 + num2
    print("El resultado es: " + str(resultado))
elif operacion == 2:
    resultado = num1 - num2
    print("El resultado es: " + str(resultado))
elif operacion == 3:
    resultado = num1 * num2
    print("El resultado es: " + str(resultado))
elif operacion == 4:
    if num2 > 0 :
        resultado = num1 / num2
        print("El resultado es: " + str(resultado))
    else:
        print("La operacion no se puede relizar ")
else:
    print("Operacion no valida")
    