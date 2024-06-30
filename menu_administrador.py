from funcionesGlobales import *

def usuario_o_admin():
    print("""¡BIENVENIDO, ¿COMO DESEAS INGRESAR?
          
**************************************
          
1). Administrador
2). Usuario
0). Salir

**************************************
""")
    opcion = listaOpciones("Ingrese la opcion","Numero no valido, ingrese de nuevo",2)
    return opcion

#MENÚ DE ADMINISTRADOR
def menu_administrador():
    datosLibros = leerJson("libros")
    usuarios = leerJson("usuarios")
    while True:
        print("""\n¡HOLA DE NUEVO ADMINISTRADOR!,¿QUE TE GUSTARIA HACER HOY?
**************************************
1 - Añadir libro
2 - Modificar libro
3 - Eliminar Libro
4 - Mostrar Libros
5 - Eliminar usuarios
6 - Modificar usuarios
0 - Salir""")

        opc= listaOpciones("Ingrese una opcion","Error, valor incorrecto, intentelo de nuevo",6)

        #AGREGAR UN LIBRO AL JSON "LIBROS",  NO DEVUELVE NADA
        if opc== 1:

            datos=Crear_libro(datosLibros)
            guardarJson("libros",datos)  

        elif opc== 2:
            libros = leerJson("libros")
            opcionLibro = input("Ingrese el nombre del libro que desea modificar: ")
            for libro in libros["libros"]:
                if libro["nombre"] == opcionLibro:
                    datos = modificar_libro(libros,opcionLibro)
                    guardarJson("libros",datos)
        
        elif opc==3:
            datosLibros = eliminar_libro(datosLibros)
            guardarJson("libros",datosLibros)
        
        elif opc == 4:
            mostrar_libros(datosLibros)
        
        elif opc == 5:
            usuarios = eliminar_usuarios(usuarios)
            guardarJson("usuarios",usuarios)
        
        elif opc== 6:
            imprimir = True
            opcionUsuarios = listaOpciones("Ingrese el documento del usuario que desea modificar","Solo se permiten numeros, intentelo de nuevo")
            for usuario in usuarios:
                if usuario["documento"] == opcionUsuarios:
                    usuarioModificado = modificar_usuarios(usuario)
                    usuarios[usuarios.index(usuario)] = usuarioModificado
                    guardarJson("usuarios",usuarios)
                    imprimir = False
            if imprimir:
                print("Documento no encontrado")
        
        elif opc==0:
            print("")
            break
        input("Oprima Enter para continuar ")
        
def modificar_usuarios(usuario):
    print("¿Que quieres modificar?")
    print("**************************************")
    print("1). Nombre")
    print("2). Edad")
    print("3). Correo Electronico")
    print("4). Libros comprados")
    print("5). Tipo cliente")
    print("0). salir")
    opcion = listaOpciones("Ingrese la opcion deseada","Opcion no valida, intentelo de nuevo",5)
    if opcion == 1:
        usuario["nombre"] = input("Ingrese el nuevo nombre que desea: ")
    elif opcion == 2:
        usuario["edad"] = listaOpciones("Ingrese la nueva edad","Edad no valida, intentelo de nuevo",99)
    elif opcion == 3:
        usuario["email"] = input("Ingrese el nuevo correo de recuperación: ")
    elif opcion == 4:
        if len(usuario["libros"]) != 0:
            for libro in range(len(usuario["libros"])):
                print(str(libro + 1) + " - " + usuario["libros"][libro])
            print("0 - Salir")
            libroOpcion = listaOpciones("Ingrese el numero del libro que desea eliminar","Numero no valido, intentelo de nuevo",len(usuario["libros"]))
            if libroOpcion != 0:
                usuario["libros"].remove(usuario["libros"][libroOpcion - 1])
        else:
            print("Este usuario no tiene libros comprados")
    elif opcion == 5:
        pass
    return usuario

def eliminar_usuarios(usuarios):
    for usuario in range(len(usuarios)):
        print(str(usuario + 1) + " - " + usuarios[usuario]["nombre"])
    print("0 - Salir")
    eliminar_usuario = listaOpciones("Ingrese el numero del usuario a eliminar","Numero no valido, ingreselo de nuevo",len(usuarios))
    if eliminar_usuario != 0:
        usuarios.remove(usuarios[eliminar_usuario - 1])
    return usuarios

def contraseña_admin():
    contra="admin12345"
    ingresar=input("Ingresa la contraseña: ")
    if ingresar == contra:
        return True
    else:
        print("*Contraseña incorrecta\n")
        return False

#****************** CRUD LIBROS ******************#

# C-REATE 
def Crear_libro(libros):
    categorias_list=leerJson("categorias")
    nombre_agregar_libro=input("Ingresa el nombre del libro que deseas agregar: ")

    ### COMPROBACION PARA VERIFICAR QUE EL NOMBRE INGRESADO NO SE ENCUENTRE YA EN EL JSON###
    while True:
        comprobacion_nombre_libro=False
        for libro in libros["libros"]:
            if libro["nombre"]==nombre_agregar_libro:
                print(f"Ya se encuentra un libro de nombre: {nombre_agregar_libro}, intenta con otro libro")
                nombre_agregar_libro=input("Ingresa el nombre del libro que deseas agregar: ")
                comprobacion_nombre_libro=True
        if comprobacion_nombre_libro==False:
            break
    ##################################################################
    
    edad=listaOpciones("Ingresa la edad minima del libro para ser comprado: ","El valor ingresado debe ser un numero")
    autor=input(f"Ingresa el autor(a) del libro: {nombre_agregar_libro}: ")
    categoria=listaOpciones("""\nLos generos disponibles son:
        
1 - Accion
2 - Biografia
3 - Fantasia
4 - Ficcion
5 - Romance
0 - Salir
        
*Ingresa el genero que deseas agregar al libro""","Debes ingresar un numero entre los géneros mostrados",5)

    descripcion=input(f"Ingresa una descripcion para el libro {nombre_agregar_libro}: ")
    publicacion=listaOpciones("Ingresa el año de publicación del libro","Se debe ingresar un valor numérico")
    stock=listaOpciones(f"Ingresa la cantidad de unidades que hay del libro {nombre_agregar_libro}","Se debe ingresar un valor numérico")
    precio=listaOpciones(f"Ingresa el precio del libro","Se debe ingresar un valor numerico")
    libros["libros"].append({"nombre":nombre_agregar_libro,
                            "edad":edad,
                            "autor":autor,
                            "categoria":categoria,
                            "descripcion":descripcion,
                            "publicacion":publicacion,
                            "stock":stock,
                            "precio":precio})
    print("Se agregó correctamente el libro al json 'libros")
    return libros

# R-EAD 
def mostrar_libros(libros):
    print("")
    for libro in libros["libros"]:
        print("**********************************************")
        print("Nombre: " + libro["nombre"])
        print("Edad: " + str(libro["edad"]))
        print("Autor(a): " + libro["autor"])
        print("Categoría: " + str(libro["categoria"]))
        print("Descripción: " + libro["descripcion"])
        print("Publicación: " + str(libro["publicacion"]))
        print("Stock: " + str(libro["stock"]))
        print("Precio: " + str(libro["precio"]))
        print("**********************************************\n")


# U-PDATE
def modificar_libro(datos,nombre):
    datos=dict(datos)
    for i in range(len(datos["libros"])):
        if datos["libros"][i]["nombre"] == nombre:
            while True:
                print("¿Que te gustaria cambiar?")
                print("******************************")
                print("1). Para modificar el Nombre: ")
                print("2). Para modificar la Edad: ")
                print("3). Para modificar el Autor: ")
                print("4). Para modificar la Categoria: ")
                print("5). Para modificar la Decripcion: ")
                print("6). Para modificar la Publicacion: ")
                print("7). Para modificar el Stock: ")
                print("8). Para modificar el Precio: ")
            
                print("0). Para salir ")
                
                opc= listaOpciones(" Ingrese la opcion ","Se debe ingresar un valor numerico")

                if opc == 1:
                    datos["libros"][i]["nombre"]= input("Ingrese el nuevo Nombre: ")
                    print(" ¡NOMRBE GUARDADO CON EXITO!")
                    print("----------------------------------")

                elif opc == 2:
                    datos["libros"][i]["edad"]= listaOpciones("Ingrese la nueva Edad minima para leer el libro: ","La edad ingresada debe ser un valor númerico")
                    print(" ¡EDAD GUARDADA CON EXITO!")
                    print("----------------------------------")


                elif opc == 3:
                    datos["libros"][i]["autor"]= input("Ingrese el nuevo Autor:")
                    print(" ¡AUTOR GUARDADO CON EXITO!")
                    print("----------------------------------")


                elif opc == 4:
                    datos["libros"][i]["categoria"]= listaOpciones("Ingrese la nueva categoria: ","La categoría ingresada debe ser un valor númerico")
                    print(" ¡CATEGORIA GUARDADA CON EXITO!")
                    print("----------------------------------")


                elif opc == 5:
                    datos["libros"][i]["descripcion"]= input("Ingrese la nueva descripcion: ")
                    print(" ¡DESCRIPCION GUARDADO CON EXITO!")
                    print("----------------------------------")


                elif opc == 6:
                    datos["libros"][i]["publicacion"]= listaOpciones("Ingrese el nuevo año de publicacion: ","El año de publicación ingresado debe ser un valor númerico")
                    print(" ¡AÑO DE PUBLICACION GUARDADO CON EXITO!")
                    print("----------------------------------")


                elif opc == 7:
                    datos["libros"][i]["stock"]= listaOpciones("Ingrese el nuevo Stock:","La cantidad de stock ingresado debe ser un valor númerico")
                    print(" ¡STOCK GUARDADO CON EXITO!")
                    print("----------------------------------")

                elif opc == 8:
                    datos["libros"][i]["precio"]= listaOpciones("Ingrese el nuevo Precio","El precio ingresado debe ser un valor númerico")
                    print(" ¡PRECIO GUARDADO CON EXITO!")
                    print("----------------------------------")
                
                
                elif opc == 0:
                    break
            break
    return datos   

# D-ELETE libro
def eliminar_libro(datos):
    datos = dict(datos)
    ref =input("Ingrese el nombre de el libro a eliminar: ")
    for i in range(len(datos["libros"])):
        if datos["libros"][i]["nombre"] == ref:
            opc=int(input("Esta seguro que desea eliminar este libro ( 1 ) Si ( 2 ) No "))
            if opc ==1:
                datos["libros"].pop(i)
                print("plan eliminado!")
                return datos
            elif opc ==2:
                print("Cancelado con exito")
                return datos

    print("plan o paquete no encontrado")
    return datos