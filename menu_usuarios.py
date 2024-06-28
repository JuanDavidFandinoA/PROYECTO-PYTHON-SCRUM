from funcionesGlobales import *
CAT_ACCION=1
CAT_BIOGRAFIA=2
CAT_FANTASIA=3
CAT_FICCION=4
CAT_ROMANCE=5


def menu_usuarios():
    while(True):
        print("""Ingreso de usuario exitoso

********************************************************

1 - Acceder al buscador de libros
2 - Acceder a los generos disponibles
3 - Comprar libros
0 - Salir

********************************************************
""")
        opcion = listaOpciones("Ingrese la opcion que desea escoger","Por favor ingrese una opcion valida",3)
        print("\n********************************************************\n")
        
        if opcion == 1:
            buscador()
        elif opcion==2:
            mostrar_generos()
        elif opcion==3:
            comprar_libro()
        else:
            print("Salida exitosa :) \n")
            break
        input("Oprima Enter para continuar\n")



    
def buscador():
    nombre = input("Ingrese el nombre del libro que desea buscar: ")
    nombre=nombre.title()
    
    datos_libros=leerJson("libros")
    for libro in datos_libros:
        if libro["nombre"]==nombre:
            print("\n***************************************************************\n")
            print("Se encontrò el libro de nombre: {nombre}, los datos de este libro son:")
            print("Nombre: " + libro["nombre"])
            print("Id: " + str(libro["id"]))
            print("Edad: " + str(libro["edad"]))
            print("Autor(a): " + libro["autor"])
            print("Categoria: " + str(libro["categoria"]))
            print("Descripcion: " + libro["descripcion"])
            print("Publicacion: " + str(libro["publicacion"]))
            return None
    print(f"No se encontrò el libro de nombre: {nombre}")

def mostrar_generos():
    print("""Los generos disponibles son:
          
1 - Accion
2 - Biografia
3 - Fantasia
4 - Ficcion
5 - Romance
0 - Salir
          
*******************************************************
""")
    generos_disponibles = leerJson("categorias")
    genero_escogido = listaOpciones("Ingrese el numero del genero que desea buscar","Por favor ingrese un numero valido",5)
    if genero_escogido == 0:
        print("")
        return None
    genero_print = generos_disponibles.get(str(genero_escogido))

    libros = leerJson("libros")

    print("\n-------------------------------------------------------\n")
    print(f"Los libros encontrados para el genero {genero_print} son: \n")
    for libro in libros:
        if libro.get("categoria") == genero_escogido:
            print("Nombre: " + libro["nombre"])
    print("\n-------------------------------------------------------\n")

def comprar_libro():
    None

menu_usuarios()

"/bin/python /run/media/mmcblk0p1/IdeaProjects/PROYECTO-PYTHON-SCRUM/menu-usuarios.py"