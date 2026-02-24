#indexing, slicing, stride  
# lista de tereas
lista_tareas = ["tarea1", "tarea2", "tarea3", "tarea4", "tarea5"]

#tupla de tareas
tupla_tareas = ("tarea1", "tarea2", "tarea3", "tarea4", "tarea5")

#diccionario de tareas
diccionario_tareas = {
"tarea1": "pendiente", 
"tarea2":"en progreso",
"tarea3":"pendiente",
"tarea4":"terninada",
"tarea5":"en progreso"
}
lista_tareas[2] = "tarea3 modificada" #se puede modificar una lista

print(f"\n lista_tareas: {lista_tareas}") 
print(" ")
#stride es la cantidad de elementos que se deben saltar entre cada elemento seleccionado. Se utiliza el operador de slicing [inicio:fin:paso] para especificar el rango de elementos que se desea obtener. El índice de inicio es inclusivo, mientras que el índice de fin es exclusivo. El paso es opcional y se utiliza para especificar la cantidad de elementos que se deben saltar entre cada elemento seleccionado.
print(f"********* Stride *********")
print(lista_tareas[0:5:2]) #tarea1, tarea3, tarea5
print(tupla_tareas[0:5:2]) #tarea1, tarea3, tarea5
#print(diccionario_tareas["tarea1":"tarea5:2"]) #no se puede hacer slicing en diccionarios, pero se puede acceder a los
print(" ")



#slicing es la forma de obtener una parte de una secuencia, como una lista, tupla o cadena. Se utiliza el operador de slicing [inicio:fin:paso] para especificar el rango de elementos que se desea obtener. El índice de inicio es inclusivo, mientras que el índice de fin es exclusivo. El paso es opcional y se utiliza para especificar la cantidad de elementos que se deben saltar entre cada elemento seleccionado.
print(f"********* Slicing *********")
print(lista_tareas[1:4]) #tarea2, tarea3, tarea4
print(tupla_tareas[1:4]) #tarea2, tarea3, tarea4
#print(diccionario_tareas["tarea2":"tarea4"]) #no se puede hacer slicing en diccionarios, pero se puede acceder a los valores mediante las claves.   
print(" ")





#indexing
print(f"********* Indexing *********")
print(lista_tareas[0]) #tarea1
print(lista_tareas[-1]) #tarea5
print(lista_tareas[1][1]) #tarea2 -> a
print(tupla_tareas[0]) #tarea1
print(diccionario_tareas["tarea1"]) #pendiente  

