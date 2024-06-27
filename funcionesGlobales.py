import json

def listaOpciones(mensaje, error, maximo):
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