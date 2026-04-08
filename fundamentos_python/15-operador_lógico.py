''' 
Operado l lógico se utilizan para combinar expresiones booleanas y obtener un resultado también booleano. Los operadores lógicos más comunes son:
'''

numero1 = 10
numero2 = 5 
#Operadores lógicos
print(f"\n********* Operadores Lógicos *********")
print(f"({numero1} > {numero2}) and ({numero1} < {numero2}) : {(numero1 > numero2) and (numero1 < numero2)}") #El operador lógico AND devuelve True si ambas expresiones son verdaderas y False en caso contrario. En este caso, como 10 es mayor que 5 pero no es menor que 5, el resultado será False.
print(f"({numero1} > {numero2}) or ({numero1} < {numero2}) : {(numero1 > numero2) or (numero1 < numero2)}") #El operador lógico OR devuelve True si al menos una de las expresiones es verdadera y False si ambas son falsas. En este caso, como 10 es mayor que 5, el resultado será True.
print(f"not ({numero1} > {numero2}) : {not (numero1 > numero2)}") #El operador lógico NOT invierte el valor de la expresión. Devuelve True si la expresión es falsa y False si la expresión es verdadera. En este caso, como 10 es mayor que 5, la expresión (numero1 > numero2) es verdadera, por lo que el resultado de not (numero1 > numero2) será False.   
        