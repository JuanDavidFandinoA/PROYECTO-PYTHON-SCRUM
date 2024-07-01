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
            return documento_pedido

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
                    return documento_pedido
    if encontrado==False:
        print(f"*No se encontrò un usuario con numero de documento {documento_pedido}")
        documento_pedido=0
        return documento_pedido
#menu usuarios
def menu_usuarios(documento_usuario):
    while True:
        print("""********************************************************

1 - Acceder al buscador de libros
2 - Acceder a los generos disponibles
3 - Comprar libros
4 - Ver el carrito
0 - Salir

********************************************************
""")
        opcion = listaOpciones("Ingrese la opcion que desea escoger","Por favor ingrese una opcion valida",4)
        print("\n********************************************************\n")
        
        if opcion == 1:
            buscador()
        elif opcion==2:
            mostrar_generos()
        elif opcion==3:
            comprar_libro(documento_usuario)
        elif opcion==4:
            carrito(documento_usuario)
        else:
            print("Salida exitosa :) \n")
            break
        input("Oprima Enter para continuar\n")

def carrito(documento):
    print("""
********************************************************
          
1 - Enlistar libros en el carrito
2 - Comprar los libros del carrito
0 - Salir
          
********************************************************
""")
    opcion = listaOpciones("Elija la opcion deseada","Opcion no valida, intentelo de nuevo",2)
    usuarios = leerJson("usuarios")
    for usuario in usuarios:
        if usuario.get("documento") == documento:
            if opcion == 1:
                if len(usuario.get("libros")) != 0:
                    for libro in range(len(usuario.get("libros"))):
                        print(str(libro + 1) + " - " + usuario.get("libros")[libro])
                    print("0 - Salir")
                    opcionLibro = listaOpciones("Si desea eliminar un libro ingrese su numero, o ingrese 0 para salir","Opcion no valida",len(usuario.get("libros")))
                    if opcionLibro != 0:
                        usuarios[usuarios.index(usuario)]["libros"].remove(
                        usuario["libros"][opcionLibro - 1])
                    else:
                        print("Salida exitosa")
                    guardarJson("usuarios",usuarios)
                else:
                    print("Usted no tiene libros en el carrito!")
            if opcion == 2:
                if len(usuario.get("libros")) == 0:
                    print("Usted no tiene libros en el carrito!")
                usuarios[usuarios.index(usuario)]["libros"] = []
                guardarJson("usuarios",usuarios)

def buscador():
    nombre = input("Ingrese el nombre del libro que desea buscar: ")
    
    datos_libros=leerJson("libros")
    for libro in datos_libros["libros"]:
        if (libro["nombre"]).lower()==nombre.lower():
            print("\n***************************************************************\n")
            print("Se encontrò el libro de nombre: " + libro["nombre"] + ", los datos de este libro son:")
            print("Nombre: " + libro["nombre"])
            print("Edad: " + str(libro["edad"]))
            print("Autor(a): " + libro["autor"])
            print("Categoria: " + str(libro["categoria"]))
            print("Descripcion: " + libro["descripcion"])
            print("Publicacion: " + str(libro["publicacion"]))
            print("Precio: " + str(libro["precio"]))
            return libro["nombre"]
    print(f"No se encontrò el libro de nombre: {nombre}")
    nombre=False
    return nombre

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
    for libro in libros["libros"]:
        if libro.get("categoria") == genero_escogido:
            print("Nombre: " + libro["nombre"])
    print("\n-------------------------------------------------------\n")

def mostrar_generos__compra(documento_user):
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
    
    usuarios=leerJson("usuarios")
    
    if genero_escogido == 0:
        print("")
        return None
    genero_print = generos_disponibles.get(str(genero_escogido))

    libros = leerJson("libros")
    lista_libros=[]
    print("\n-------------------------------------------------------\n")
    print(f"Los libros encontrados para el genero {genero_print} son: \n")
    contador=1
    for libro in libros["libros"]:
        if libro.get("categoria") == genero_escogido:
            lista_libros.append(libro["nombre"])
            print(str(contador) + " - " + libro["nombre"])
            contador+=1
    libro_escogido=listaOpciones("Escoge el numero de libro que deseas comprar o '0' para salir","Se debe ingresar un valor de los dados",contador-1)
    if libro_escogido==0:
        return None
    
    nombre_libro=lista_libros[libro_escogido-1]
    print("el libro escogido fue: " + lista_libros[libro_escogido-1])
    
    ############### AGREGAR AL CARRITO ###############################
    print("""\n*¿Deseas agregar el libro """+nombre_libro+""" al carrito?:

********************************************************

1 - Sí
2 - No
0 - salir

********************************************************
""")

    opcion_carrito=listaOpciones("Ingresa la opcion que deseas escoger","El valor ingresado debe pertenecer a las ocpiones",2)
    
    if opcion_carrito==1:
        #################### AGREGAR LIBRO AL USUARIO #################
        for user in usuarios:
            if user["documento"]==documento_user:
                user["libros"].append(nombre_libro)
        print("-Libro agregado correctamente al carrito")
        ################### QUITAR UN LIBRO DEL STOCK ###############
        for libro in libros["libros"]:
            if libro["nombre"]==nombre_libro:
                libro["stock"]-=1
        guardarJson("usuarios",usuarios)
        guardarJson("libros",libros)
    elif opcion_carrito==2:
        None
    else:
        print("Salida exitosa ")

def comprar_libro(documento_user):
    libros=leerJson("libros")
    usuarios=leerJson("usuarios")
    while True:
        print("""\nLas opciones de busqueda para comprar libro son:

********************************************************

1 - Buscar por nombre del libro
2 - Buscar por categorias
0 - Salir

********************************************************
""")
        modo_opcion=listaOpciones("Ingresa la opción que desees","El valor ingresado debe pertenecer a las ocpiones",2)
        
        if modo_opcion==1:
            nombre_libro=buscador()
            #### Nombre_libro=False si no se encontró el libro en el json#####
            if nombre_libro!=False:
            
                print("""\n*¿Deseas agregar este libro al carrito?:

********************************************************

1 - Sí
2 - No
0 - salir

********************************************************
""")
                
                opcion_carrito=listaOpciones("Ingresa la opcion que deseas escoger","El valor ingresado debe pertenecer a las ocpiones",2)
                
                if opcion_carrito==1:
                    #################### AGREGAR LIBRO AL USUARIO #################
                    for user in usuarios:
                        if user["documento"]==documento_user:
                            user["libros"].append(nombre_libro)
                    print("-Libro agregado correctamente al carrito")
                    ################### QUITAR UN LIBRO DEL STOCK ###############
                    for libro in libros["libros"]:
                        if libro["nombre"]==nombre_libro:
                            libro["stock"]-=1
                    guardarJson("usuarios",usuarios)
                    guardarJson("libros",libros)
                elif opcion_carrito==2:
                    None
                else:
                    print("Salida exitosa")
        elif modo_opcion==2:
            mostrar_generos__compra(documento_user)
        else:
            print("Salida exitosa del modulo comprar")
            break

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
    print("¡Cliente registrado con éxito!\n")
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
            guardarJson("usuarios",datos)
        elif opcion == 2:
            documento_usuario=iniciar_sesion()
            if documento_usuario!=0:
                menu_usuarios(documento_usuario)
        else:
            print("Saliste exitosamente")
            return datos