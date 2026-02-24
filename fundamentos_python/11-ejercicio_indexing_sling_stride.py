'''
# 1. Creación del Menú
 
# Creando la lista de platos
platos = ["Paella", "Risotto", "Sushi", "Tacos", "Pizza"]
 
# Creando la tupla de precios
precios = (15, 12, 20, 10, 8)
 
# Utilizando slicing para seleccionar platos
platos_seleccionados = platos[1:4]  # Del segundo al cuarto plato
 
# Creando el diccionario del menú
menu = {
    platos[0]: precios[0],
    platos[1]: precios[1],
    platos[2]: precios[2],
    platos[3]: precios[3],
    platos[4]: precios[4]
}
 
# 2. Exploración del Menú
 
# Imprimiendo el menu completo
 
# NOTA: En Python, los paréntesis se pueden usar para varias cosas, 
# incluyendo la definición de tuplas. Sin embargo, también se 
# utilizan para agrupar expresiones o, como en este caso, para extender 
# una línea de código a varias líneas para mejorar la legibilidad. 
descripcion_menu = (
    f"Bienvenidos a nuestro menú especial: "
    f"\n - Paella:{menu['Paella']} euros"
    f"\n - Risotto: {menu['Risotto']} euros"
    f"\n - Sushi: {menu['Sushi']} euros"
    f"\n - Tacos: {menu['Tacos']} euros"
    f"\n - Pizza: {menu['Pizza']} euros"
)
print(descripcion_menu)
 
# Imprimiendo el nombre y precio del tercer plato
tercer_plato = platos[2]
precio_tercer_plato = menu[tercer_plato]
print(f"El tercer plato es {tercer_plato} y su precio es {precio_tercer_plato}.")
 
# Utilizando stride para obtener platos en posiciones pares
platos_pares = platos[0::2]
print(f"Los platos pares son: {platos_pares}")

'''
#1, Creación del Menú
# Creando la lista de platos
platos = ["Paella", "Risotto", "Sushi", "Tacos", "Pizza"]   
# Creando la tupla de precios
precios = (15, 12, 20, 10, 8)
# Utilizando slicing para seleccionar platos
platos_seleccionados = platos[1:4]  # Del segundo al cuarto plato
# Creando el diccionario del menú
menu = {
    platos[0]: precios[0],
    platos[1]: precios[1],
    platos[2]: precios[2],
    platos[3]: precios[3],
    platos[4]: precios[4]
}
#2, Exploración del Menú
# Imprimiendo el menu completo
descripcion_menu = (
    f"Bienvenidos a nuestro menú especial: "
    f"\n - Paella:{menu['Paella']} euros"
    f"\n - Risotto: {menu['Risotto']} euros"
    f"\n - Sushi: {menu['Sushi']} euros"
    f"\n - Tacos: {menu['Tacos']} euros"
    f"\n - Pizza: {menu['Pizza']} euros"
)
print(descripcion_menu)
# Imprimiendo el nombre y precio del tercer plato
tercer_plato = platos[2]
precio_tercer_plato = menu[tercer_plato]
print(f"El tercer plato es {tercer_plato} y su precio es {precio_tercer_plato}.")
# Utilizando stride para obtener platos en posiciones pares
platos_pares = platos[0::2]
print(f"Los platos pares son: {platos_pares}")          


