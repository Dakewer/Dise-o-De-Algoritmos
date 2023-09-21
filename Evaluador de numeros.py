#TAREA 10 Números_primos
import math
print("inserte el numero a analizar \n")
flag = False
evaluar = int(input())
for i in range (2, int(math.sqrt(evaluar)) + 1):
    if evaluar % i == 0:
        flag = True
        break
if flag: 
    print("No es primo\n")
else:
    print("Es primo\n")