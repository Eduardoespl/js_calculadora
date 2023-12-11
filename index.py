print("*** Calculadora Basica ***")
print(" ")
#En esta primer parte se capturan los numero.
print("Ingresa el primer numero")
num1 = int(input())
print("Ingresa el segundo numero")
num2 = int(input())
#Una vez se capturan los datos se despliega un pequeno menu
#para que el ususario elija la operacion.
print("Ingresa la operacion que deseas realizar")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Residuo")
print("6. Salir")
operacion = int(input())

#Aqui estan las operaciones y la logica de las operaciones
# 1 Esta es la operacion logica de la suma . 
if operacion == 1:
    resultado = num1 + num2
    print("El resultado es: " + str(resultado))
# 2Esta es la operacion logica de la resta 
elif operacion == 2:
    resultado = num1 - num2
    print("El resultado es: " + str(resultado))
#3 Esta es la operacion logica de la multiplicacion. 
elif operacion == 3:
    resultado = num1 * num2
    print("El resultado es: " + str(resultado))
# 4 Esta es la operacion logica de la division.
elif operacion == 4:
    if num2 > 0 :
        resultado = num1 / num2
        print("El resultado es: " + str(resultado))
    else:
        print("La operacion no se puede relizar ")
elif operacion == 5:
    resultado = num1 % num2
    print("El resultado es: " + str(resultado))
elif operacion == 6:
    print("Gracias por usar la calculadora")
else:
    print("Operacion no valida")
    