#string es una cadena de texto, se representa entre comillas simples o dobles
print("Hola, soy un string con comillas dobles")
print('Hola, soy un string con comillas simples')
#int es un número entero, sin decimales no confundir numero con comillas son string
print(42)
#float es un número con decimales
print(3.14) #el punto es el separador decimal en Python, no la coma
#bool es un valor booleano, puede ser True o False
print(True)
print(False)
#utlilizar type() para conocer el tipo de dato de una variable o valor
print(type("Hola, soy un string"))
print(type(42))
print(type(3.14))
print(type(True))   

#f string es una forma de formatear cadenas de texto, se representa con una f antes de las comillas
nombre = "Marcos"
edad = 50
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")      
