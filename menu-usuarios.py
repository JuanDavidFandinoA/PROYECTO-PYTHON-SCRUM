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
    elif opcion==3:
        comprar_libro()
    else:
        print("Salida exitosa :) \n")



    
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

def mostrar_generos():
    print("""
Los generos disponibles son:
0 - Biografia
1 - Ficcion
2 - Accion
3 - Fantasia
4 - Romance

*******************************************************""")
    generos_disponibles=["biografía","ficcion","accion","fantasia","romance"]
    genero_escogido = listaOpciones("Ingrese el numero del genero que desea buscar","Por favor ingrese un numero valido",4)
    genero_escogido=generos_disponibles[genero_escogido]

    datos_ficcion=leerJson(genero_escogido)

    print(f"Los libros encontrados para el genero {genero_escogido} son: \n")
    for libro in datos_ficcion:
        print("Nombre: " + libro["nombre"])
        print("Autor(a): " + libro["autor"])
        print("Edad: " + str(libro["edad"]))
        print("Descripción: " + libro["descripcion"])
        print("\n*****************************************************\n")

def comprar_libro():
    None

menu_usuarios()