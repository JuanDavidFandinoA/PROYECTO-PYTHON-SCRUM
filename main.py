from funcionesGlobales import *
from menu_administrador import*
from menu_usuarios import*


while True:
    datosUsuarios= leerJson("usuarios")
    opc = usuario_o_admin()
    if opc == 1:
        if contraseña_admin():
            menu_administrador()
    elif opc == 2:
        login(datosUsuarios)
    elif opc== 0:
        print("Gracias por ingresar a knowledge jungle ")
        print("¡Vuelva Pronto a aprender")
        break
    else:
        print("Ingresa un valor valido")
