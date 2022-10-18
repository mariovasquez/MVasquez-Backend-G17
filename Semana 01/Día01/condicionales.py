#ENTRADA
from unittest import result


numero1 = input("Número 1 : ")
numero2 = input("Número 2 : ")
operacion = input("Operación a ejecutar : ")
#PROCESO
if(operacion == "suma"):
    resultado = int(numero1) + int(numero2)
elif(operacion == "resta"):
    resultado = int(numero1) - int(numero2)
else:
    resultado = 0
    print("Debe ingresar una operación válida")
#SALIDA
if(resultado != 0):
    print("El resultado es : " + str(resultado))