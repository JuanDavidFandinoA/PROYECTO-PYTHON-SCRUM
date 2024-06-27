from funcionesGlobales import *
from menu_administrador import*
from menu_de_usuarios import*

#constantes
#---------------
#---------------
#---------------
#---------------
#---------------
#---------------
#---------------
#---------------
#---------------
#---------------
#---------------
#---------------
#---------------
#---------------
usuario_o_admin()

while True:
    
    opc=pedir_opcion()
    if opc== 1:
        contraseña_admin()
    elif opc ==2:
        menu_usuarios()
    elif opc== 0:
        print("Gracias por ingresar a knowledge jungle ")
        print("¡Vuelva Pronto a aprender")
        break
    else:
        print("Ingresa un valor valido")

