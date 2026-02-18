'''Práctica Comentarios
Objetivo:

Aprender a documentar y explicar código en Python utilizando comentarios, basándonos en el ejercicio anterior "Diario de un Astronauta".



Instrucciones:

Toma el código proporcionado en el ejercicio "Diario de un Astronauta".

Añade comentarios adecuados a cada línea o bloque de código para explicar lo que hace. Esto incluye:

Explicar la creación y uso de variables.

Describir cómo se construyen los mensajes que se imprimen.

Mencionar cualquier detalle que consideres relevante para entender el código.

Asegúrate de que los comentarios sean claros y concisos, y que ayuden a comprender el propósito de cada parte del código.



Resultado esperado:

El código del ejercicio anterior incluyendo al menos 4 comentarios explicativos. Estos comentarios deben ayudar a entender cada paso y decisión tomada en el código.



Notas para el estudiante:

Usa comentarios para explicar por qué se hace algo, no qué se hace. El código ya muestra qué se hace.

Evita comentarios innecesarios o redundantes. Los comentarios deben añadir valor y claridad al código.

Un comentario incorrecto puede ser más perjudicial que no tener comentarios.

Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no son correctos, se desbloqueará la pestaña "Explicación de la solución" en la parte superior del ejercicio. En esta pestaña puedes ver el código de solución de esta práctica.
'''
# Definición de variables para personalizar el diario del astronauta.
nombre_astronauta = "Max"
edad_astronauta = 25
destino = "Marte"
 
# Datos de la misión, cruciales para el seguimiento del estado de la nave.
combustible = 85
velocidad = 27000
 
# Encabezado del diario para dar contexto al lector sobre el contenido.
print("Diario de un Astronauta\n")
 
# Uso de f-strings para una presentación dinámica y personalizada del diario.
print(f"Hola, soy {nombre_astronauta}, tengo {edad_astronauta} años y mi próximo destino es {destino}.\n")
 
# Información detallada del estado de la misión, esencial para el seguimiento de la nave.
print(f"Estoy navegando a {velocidad} km/s con {combustible}% de combustible restante hacia {destino}.\n")
 
# Registro de eventos diarios, importante para documentar la vida y las actividades en el espacio.
print("Fecha: 2024-01-10")
print("Hoy experimentamos con el cultivo de plantas en microgravedad.")
print("Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!\n")
 
print("Fecha: 2024-01-11")
print("Realizamos una caminata espacial para reparar un panel solar.")
print("Mensaje personal: Flotar en el espacio nunca deja de asombrarme.\n")
