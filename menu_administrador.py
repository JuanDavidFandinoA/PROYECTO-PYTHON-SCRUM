from funcionesGlobales import *

def usuario_o_admin():
    print("""¡BIENVENIDO, ¿COMO DESEAS INGRESAR?")
          
**************************************
          
1). Administrador
2). Usuario
0). Salir

**************************************
""")
    opcion = listaOpciones("Ingrese la opcion","Numero no valido, ingrese de nuevo",2)
    if opcion == 1:
        if contraseña_admin():
            menu_administrador()
    elif opcion == 2:
        pass
    else:
        return None


def menu_administrador():
    print("""¡HOLA DE NUEVO ADMINISTRADOR!,¿QUE TE GUSTARIA HACER HOY?")
    print("**************************************")
    print("1). Añadir libro")
2 - Modificar libro")
3 - Eliminar Libro")
4 - Mostrar Libros")
5 - Eliminar usuarios")
6 - Modificar usuarios")
0 - Salir""")

    opc= input("ingrese una opcion: ")
    if opc== 1:
        print()
    elif opc== 2:
        print(modificar_libro)
    elif opc==3:
        print()
    elif opc == 4:
        print()
    elif opc == 5:
        print()
    elif opc== 6:
        print(modificar_usuarios)
        


def modificar_libro():
    print("¿Que quieres modificar?")
    print("**************************************")
    print("1). Nombre")
    print("2). Edad")
    print("3). Descripcion")
    print("4). Autor")
    print("0). salir")

def modificar_usuarios():
    print("¿Que quieres modificar?")
    print("**************************************")
    print("1). Nombre")
    print("2). Edad")
    print("3). Documento")
    print("4). Libros comprados")
    print("5). Tipo cliente")
    print("0). salir")



def contraseña_admin():
    contra="admin12345"
    ingresar=input("Ingresa la contraseña: ")
    if ingresar == contra:
        return True
    else:
        print("Contraseña incorrecta\n")
        return False


def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1     

usuario_o_admin()