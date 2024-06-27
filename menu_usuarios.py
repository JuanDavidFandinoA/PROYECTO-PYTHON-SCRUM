from funcionesGlobales import *
CAT_ACCION=1
CAT_BIOGRAFIA=2
CAT_FANTASIA=3
CAT_FICCION=4
CAT_ROMANCE=5


def menu_usuarios():
    while(True):
        print("Ingreso de usuario exitoso")
        print("\n*******************************************************\n")
        print("Presiona ( 1 ) para acceder al buscador de libros")
        print("Presiona ( 2 ) para acceder a los generos disponibles")
        print("Presiona ( 3 ) para comprar libros")
        print("Presiona ( 0 ) para salir")
        print("\n*******************************************************\n")
        opcion = listaOpciones("Ingrese la opcion que desea escoger","Por favor ingrese una opcion valida",3)
        print("\n*******************************************************\n")
        
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
            print(f"Se encontrò el libro de nombre: {nombre}, los datos de este libro son:")
            print("***************************************************************")
            print("Nombre: " + libro["nombre"])
            print("Id: " + str(libro["id"]))
            print("Edad: " + str(libro["edad"]))
            print("Autor(a): " + libro["autor"])
            print("Categoria: " + str(libro["categoria"]))
            print("Descripcion: " + libro["descripcion"])
            print("Publicacion: " + str(libro["publicacion"]))
            return None
    print(f"No se encontrò el libro de nombre: {nombre}")


    # generos = ["ficcion"]
    # for genero in generos:
    #     datos = leerJson(genero)
    #     for libro in datos:
    #         if libro.get("nombre") == nombre:
    #             print("Nombre: " + libro.get("nombre"))
    #             print("Autor(a): " + libro.get("autor"))
    #             print("Edad: " + str(libro.get("edad")))
    #             print("Descripción: " + libro.get("descripcion"))
    #             return None
    # print("Libro no encontrado")

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
    generos_disponibles = leerJson("categorias").keys()
    genero_escogido = listaOpciones("Ingrese el numero del genero que desea buscar","Por favor ingrese un numero valido",5)
    if genero_escogido == 0:
        print("")
        return None
    else:
        genero_escogido -= 1
    genero_escogido = generos_disponibles[genero_escogido]

    datos_ficcion=leerJson("libros")

    print("\n-------------------------------------------------------\n")
    print(f"Los libros encontrados para el genero {genero_escogido} son: \n")
    for libro in datos_ficcion:
        print("Nombre: " + libro["nombre"])
        print("Autor(a): " + libro["autor"])
        print("Edad: " + str(libro["edad"]))
        print("Descripción: " + libro["descripcion"])
        print("\n-------------------------------------------------------\n")

def comprar_libro():
    None

menu_usuarios()

"/bin/python /run/media/mmcblk0p1/IdeaProjects/PROYECTO-PYTHON-SCRUM/menu-usuarios.py"