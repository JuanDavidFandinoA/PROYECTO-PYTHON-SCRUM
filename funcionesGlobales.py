import json

#Se ingresa un mensaje inicial, un mensaje de error, y el numero maximo para las opciones
#Se retorna un numero entre 0 y el numero maximo ingresado, en formato numero
#Si no se ingresa un numero maximo, se regresa un numero mayor a 0
#La principal funcion de esto es evitar que se ingresen letras a la hora de pedir una opcion
def listaOpciones(mensaje, error, maximo = 0):
    if maximo > 0:
        try:
            answer = int(input(mensaje + ": "))
            if(answer > maximo or answer < 0):
                answer = int("f")
        except ValueError:
            answer = None
            while (answer == None):
                try:
                    answer = int(input(error + ": "))
                    if(answer > maximo or answer < 0):
                        answer = None
                except ValueError:
                    answer = None
            
        return answer
    else:
        try:
            answer = int(input(mensaje + ": "))
            if(answer < 0):
                answer = int("f")
        except ValueError:
            answer = None
            while (answer == None):
                try:
                    answer = int(input(error + ": "))
                    if(answer < 0):
                        answer = None
                except ValueError:
                    answer = None
            
        return answer

def leerJson(nombre):
    file = open(nombre + ".json","r")
    datos = json.load(file)
    file.close()
    return(datos)

def guardarJson(nombre, datos):
    file = open(nombre + ".json","w")
    dump = json.dumps(datos,indent=4)
    file.write(dump)
    file.close()