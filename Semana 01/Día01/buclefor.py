#ENTRADA
tabla = input("Ingrese la tabla de multiplicar : ")
#PROCESO
for contador in range(1,13):
    #SALIDA
    print(tabla + " x " + str(contador) + " = " + str(contador * int(tabla)))