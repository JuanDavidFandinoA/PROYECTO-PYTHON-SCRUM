from funcionesGlobales import *

def menu_usuarios():
    print("Ingreso de usuario exitoso")
    print("*******************************************************")
    print("Presiona ( 1 ) para acceder al buscador de libros")
    print("Presiona ( 2 ) para acceder a los generos disponibles")
    print("Presiona ( 3 ) para comprar libros")
    print("Presiona ( 0 ) para salir")
    print("*******************************************************")
    opcion = listaOpciones("Ingrese la opcion que desea escoger","Por favor ingrese una opcion valida",3)
    print("*******************************************************")
    
    if opcion == 1:
        buscador()
    elif opcion==2:
        mostrar_generos()

def mostrar_generos():
    print("""
Los generos disponibles son:
0 - Biografia
1 - Ficcion
2 - Accion
3 - Fantasia
4 - Romance
*******************************************************""")
    genero_escogido = listaOpciones("Ingrese el numero del genero que desea buscar","Por favor ingrese un numero valido",4)

    datos_ficcion=leerJson(genero_escogido)
    print(datos_ficcion)
    print("Se debía ingresar un genero correcto")
    
def buscador():
    nombre = input("Ingrese el nombre del libro que desea buscar: ")
    print("")
    generos = ["ficcion"]
    for genero in generos:
        datos = leerJson(genero)
        for libro in datos:
            if libro.get("nombre") == nombre:
                print("Nombre: " + libro.get("nombre"))
                print("Autor(a): " + libro.get("autor"))
                print("Edad: " + str(libro.get("edad")))
                print("Descripción: " + libro.get("descripcion"))
                return None
    print("Libro no encontrado")

menu_usuarios()