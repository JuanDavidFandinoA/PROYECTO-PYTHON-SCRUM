from funcionesGlobales import *
#menu para iniciar sesion
def iniciar_sesion():
    datos= leerJson("usuarios")
    sesion_iniciada=False
    print("-------------------------------------------------------------------------")
    print("")
    print("¡Inicia sesión para comenzar la aventura!\n".center(70))
    print("-------------------------------------------------------------------------")
    print("")

    documento_pedido = listaOpciones("Ingresa tu número de documento","Error, solo se permiten numeros")
    while len(str(documento_pedido)) != 10:
        documento_pedido = listaOpciones("¡Documento no válido!, intentálo de nuevo o ingresa '0' para salir","Error, solo se permiten numeros")
        if documento_pedido == 0:
            print ("\nDecidiste salir de iniciar sesión, ádios!")
            return None

    encontrado = False
    for usuario in datos:
            if documento_pedido == usuario["documento"]:
                encontrado=True
                contrasena_pedida= input("Ingresa tu contraseña: ")

                while contrasena_pedida != usuario["contrasena"]:
                    contrasena_pedida = input("\nContraseña incorrecta!, Intentálo de nuevo o ingresa '0' para salir de iniciar sesión: ")
                    if contrasena_pedida == "0":
                        print ("\nDecidiste salir de iniciar sesión, ádios!")
                        break
                if contrasena_pedida == usuario["contrasena"]:
                    print(f"\nHola {usuario['nombre']}, es un placer tenerte de vuelta!")
                    sesion_iniciada=True
                    return sesion_iniciada
    if encontrado==False:
        print(f"*No se encontrò un usuario con numero de documento {documento_pedido}")
#menu usuarios
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
    
#Recibe datos de usuarios actuales, añade usuario nuevo, regresa datos con usuario añadido
def registrar_usuario(datos):
    usuario = {}
    usuario["nombre"] = input("Ingrese el nombre: ")
    documento_usuario_temp= listaOpciones("Ingrese el documento","Error, documento no valido")

    while True:
        comprobacion_documento=False
        for users in datos:
            if users["documento"]==documento_usuario_temp:
                print(f"Ya se encuentra un usuario con documento: {documento_usuario_temp}")
                documento_usuario_temp= listaOpciones("Ingrese el documento","Error, documento no valido")
                comprobacion_documento=True
            if len(str(documento_usuario_temp))!=10:
                print("El documento ingresado debe contener 10 numeros")
                documento_usuario_temp= listaOpciones("Ingrese el documento","Error, documento no valido")
                comprobacion_documento=True  
        if comprobacion_documento==False:
            break
        
    usuario["documento"] = documento_usuario_temp
    usuario["contrasena"] = input("Ingrese su contraseña: ")
    usuario["email"] = input("Ingrese un correo de recuperación: ")
    usuario["edad"] = listaOpciones("Ingrese la edad","Edad no valida, intentelo de nuevo",99)
    usuario["libros"]=[]
    
    datos.append(usuario)
    print("¡Cliente registrado con éxito!")
    return datos

def pantalla_principal():
    print("( 1 ) Para registrase")
    print("( 2 ) Para iniciar sesión")
    print("( 0 ) Para salir")

#Recibe datos de usuarios actuales, regresa datos modificados
def login(datos):
    while True:
        pantalla_principal()
        opcion = listaOpciones("Ingrese la opcion que desea","Error, opcion no valida, intentelo de nuevo",2)
        if opcion == 1:
            datos=registrar_usuario(datos)
            return datos
        elif opcion == 2:
            iniciar_sesion()
        else:
            print("Saliste exitosamente")
            return datos