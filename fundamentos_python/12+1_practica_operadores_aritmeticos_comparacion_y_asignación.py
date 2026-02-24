'''
Práctica Operadores Aritméticos, Comparación y Asignación
Objetivo:

Desarrollar un script que calcule la puntuación final de un participante en una competición de ciberseguridad, utilizando operadores aritméticos, de comparación y de asignación.



Instrucciones:

Define tres variables numéricas que almacenan los resultados del alumno:

puntuacion_pentesting

puntuacion_analisis_vulnerabilidades

puntuacion_desarrollo_exploits

Define tres variables numéricas que representen los pesos de cada una de las puntuaciones:

peso_pentesting: 50%

peso_analisis_vulnerabilidades: 20%

peso_desarrollo_exploits: 30%

Define una variable llamada puntuacion_final que calcule mediante operadores aritméticos la puntuación del alumno sumando las puntuaciones ponderadas según su peso.

Define una variable llamada participante_aprobado que, mediante operadores de comparación, se le asigne el valor True o False dependiendo de si la puntuacion_final es superior o igual a 5.

Define una variable llamada distincion_honor que, mediante operadores de asignación, compruebe si la puntuacion_final es igual a 10 y le asigne el valor True o False en función e ello.

Mediante print imprime la puntuacion_final, participante_aprobado y matricula_honor de la siguiente forma:

La calificación final es: X

¿Alunno aprobado?: X

¿Matrícula de honor: X?



Resultado esperado:

La puntuación final es: 6.1

¿Participante aprobado?: True

¿Distinción de honor?: False



Notas para el estudiante:

Para aprobar esta evaluación tu respuesta debe coincidir con los datos presentados en la sección "Resultado esperado".

Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no son correctos, se desbloqueará la pestaña "Explicación de la solución" en la parte superior del ejercicio. En esta pestaña puedes ver el código de solución de esta práctica.

'''
# Definición de variables numéricas para las puntuaciones del alumno
puntuacion_pentesting = 7.5
puntuacion_analisis_vulnerabilidades = 6.0
puntuacion_desarrollo_exploits = 8.0 
# Definición de variables numéricas para los pesos de cada puntuación
peso_pentesting = 0.5
peso_analisis_vulnerabilidades = 0.2
peso_desarrollo_exploits = 0.3
# Cálculo de la puntuación final utilizando operadores aritméticos
puntuacion_final = (puntuacion_pentesting * peso_pentesting) + (puntuacion_analisis_vulnerabilidades * peso_analisis_vulnerabilidades) + (puntuacion_desarrollo_exploits * peso_desarrollo_exploits)
# Asignación de valor a participante_aprobado utilizando operadores de comparación
participante_aprobado = puntuacion_final >= 5
# Asignación de valor a distincion_honor utilizando operadores de asignación
distincion_honor = puntuacion_final == 10
# Impresión de los resultados
print(f"La puntuación final es: {puntuacion_final}")
print(f"¿Participante aprobado?: {participante_aprobado}")
print(f"¿Distinción de honor?: {distincion_honor}")
            