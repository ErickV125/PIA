def obj(objeto,hasta ,valor , tipo = '',retornar_posicion = False):
    posicion = 0;pos_anterior = '';pos_siguente = '';lectura = '';leer = False;
    for indice in range(len(objeto)):
        caracter_actual = objeto[indice]
        if caracter_actual == '[': posicion+=1
        if posicion == hasta: leer = True
        if leer: lectura += caracter_actual
        if caracter_actual == ']' and leer: leer = False
        elif pos_anterior < hasta: pos_anterior+= caracter_actual         
        else: pos_siguente+=caracter_actual
    if retornar_posicion: return posicion
    match tipo:
        case 'leer':
            return leer()
        case 'buscar':
            return buscar()
        case 'modificar':
            return modificar()