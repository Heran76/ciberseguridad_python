numero1 = 10
numero2 = 5

string_1 = "Hola"
string_2 = "Mundo"

lista_1 = ["valor1", "valor2","valor3"]
lista_2 = ["valor3", "valor4","valor5"]

dict_1 = {"clave1": "valor1", "clave2": "valor2"}
dict_2 = {"clave3": "valor3", "clave4": "valor4"}

#Operadores aritméticos
print(f"\n********* Operadores Aritméticos *********")
#Suma
print(f"Suma: {numero1} + {numero2} = {numero1 + numero2}")#suma de numeros 
print(f"Suma de strings: {string_1} + {string_2} = {string_1 + ' ' + string_2}") #suma de strings, se puede concatenar utilizando el operador + y agregando un espacio entre ellos para mejorar la legibilidad.
print(f"Suma de listas: {lista_1} + {lista_2} = {lista_1 + lista_2}")
#print(f"Suma de diccionarios: {dict_1} + {dict_2} = {dict(dict_1, **dict_2)}") #no se puede sumar diccionarios, pero se puede combinar utilizando el operador de desempaquetado **.
print(f"resta: {numero1} - {numero2} = {numero1 - numero2}") #resta de numeros
print(f"Multiplicación: {numero1} * {numero2} = {numero1 * numero2}") #multiplicación de numeros
print(f"División: {numero1} / {numero2} = {numero1 / numero2}") #división de numeros
print(f"División entera: {numero1} // {numero2} = {numero1 // numero2}") #división entera de numeros
print(f"Resto: {numero1} % {numero2} = {numero1 % numero2}") #resto de numeros
print(f"Potencia: {numero1} ** {numero2} = {numero1 ** numero2}") #potencia de numeros

#Operadores de comparación
print(f"\n********* Operadores de Comparación *********")
print(f"{numero1} == {numero2} : {numero1 == numero2}") #El operador de igualdad (==) se utiliza para comparar dos valores y devuelve True si son iguales y False si no lo son. En este caso, como 10 no es igual a 5, el resultado será False.
print(f"{numero1} != {numero2} : {numero1 != numero2}") #El operador de desigualdad (!=) se utiliza para comparar dos valores y devuelve True si no son iguales y False si son iguales. En este caso, como 10 no es igual a 5, el resultado será True.
print(f"{numero1} > {numero2} : {numero1 > numero2}")#El operador de mayor que (>) se utiliza para comparar dos valores y devuelve True si el valor de la izquierda es mayor que el valor de la derecha y False en caso contrario. En este caso, como 10 es mayor que 5, el resultado será True.
print(f"{numero1} < {numero2} : {numero1 < numero2}")# El operador de menor que (<) se utiliza para comparar dos valores y devuelve True si el valor de la izquierda es menor que el valor de la derecha y False en caso contrario. En este caso, como 10 no es menor que 5, el resultado será False.
print(f"{numero1} >= {numero2} : {numero1 >= numero2}")#El operador de mayor o igual que (>=) se utiliza para comparar dos valores y devuelve True si el valor de la izquierda es mayor o igual que el valor de la derecha y False en caso contrario. En este caso, como 10 es mayor que 5, el resultado será True.
print(f"{numero1} <= {numero2} : {numero1 <= numero2}")#El operador de menor o igual que (<=) se utiliza para comparar dos valores y devuelve True si el valor de la izquierda es menor o igual que el valor de la derecha y False en caso contrario. En este caso, como 10 no es menor ni igual que 5, el resultado será False.    

