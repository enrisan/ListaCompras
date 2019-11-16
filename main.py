# Este programa consta de un ejercicio para definir funciones
# Las actividades de cada función se enlistan en un menú
# Las tres funciones corresponden a las tres primeras opciones de un 
# menú en un ciclo while, la cuarta opción es la salida.
#
# Agregar artículos / Remover artículos / Ver artículos
#
# No tiene ningún mecanismo de validación.
# trabaja en terminal.

lista_articulos = list()

def agregar_articulo():
    articulo = input("Nombre del artículo a agregar: ")
    lista_articulos.append(articulo.capitalize())
    print("Artículo agregado")
    print()

def remover_articulo():
    print()
    articulo = input("Nombre del artículo a remover: ")
    lista_articulos.remove(articulo.capitalize())
    print("El artículo ha sido removido")

def ver_articulos():
    print()
    print("-----------Lista de Compras--------------")
    for articulo in lista_articulos:
        print(articulo)
    print("-----------------------------------------")
    print()

print("Bienvenido a la lista de compras")
print()

while True:
    print("estas son las operaciones que puedes realizar")
    print("1 - Agregar articulo")
    print("2 - Remover articulo")
    print("3 - Ver los articulos")
    print("4 - Salir")

    operacion = int(input(": "))

    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulos()
    else:
        break

print()
print("Gracias por usar nuestra Lista de Compras")
print("¡Vuelve Pronto!")
