def listaOpciones(mensaje, error, maximo):
    try:
        answer = int(input(mensaje + ": "))
        if(answer > maximo):
            answer = int("f")
    except ValueError:
        answer = None
        while (answer == None):
            try:
                answer = int(input(error + ": "))
                if(answer > maximo):
                    answer = None
            except ValueError:
                answer = None
        
    return answer

respuesta = listaOpciones("Ingrese el numero que desea","Por favor ingrese una opcion valida",7)
print(respuesta)