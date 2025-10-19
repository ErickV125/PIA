cuentas = '';nips = '';saldos = '';nombres= ''
cajero_saldo = 0;total_depositado = 0; total_retirado = 0; cambios_de_nip = 0; total_cuentas = 0
menu_escala = 50;patron_superior = '■';patron_lateral = '■';padding = 2
def menus(text,centrar = False,border_top = False,border_bottom = False):
    if border_top:
        print(patron_lateral,int((menu_escala)/len(patron_superior)-4)*patron_superior,patron_lateral)  
    if(centrar):
        espacios = int(menu_escala/2 - len(text)/2 - len(patron_lateral))
        extra = len(text) % 2
        print(f"{patron_lateral}{espacios*' '}{text}{(espacios+extra)*' '}{patron_lateral}")
    else:
        espacios = (menu_escala - len(patron_lateral)*2 - padding - len(text) )
        print(f"{patron_lateral}{padding*' '}{text}{espacios*' '}{patron_lateral}")
    if border_bottom:
        print(patron_lateral,int((menu_escala)/len(patron_superior)-4)*patron_superior,patron_lateral)
def leer(objeto,hasta_posicion):
    valor = ''
    leer = False
    posicion = 0
    for indice in range(len(objeto)):
        caracter_actual = objeto[indice]
        if caracter_actual == '[':
            posicion+=1
            if posicion == hasta_posicion:
                leer = True
        elif caracter_actual == ']' and leer:
            return valor
        elif leer:
            valor+= caracter_actual
def buscar(objeto,valor,retornar_posicion = False):
    posicion = 1
    for cuenta in range(total_cuentas):
        if leer(objeto,cuenta+1) == str(valor) and retornar_posicion == False:
            return True
        elif leer(objeto,cuenta+1) == str(valor) and retornar_posicion:
            return posicion
        posicion+=1
    else: return False
def filtrar(texto,tipo):
    valor = ''
    for posicion in texto:
        if posicion == '0' or posicion == '1' or posicion == '2' or posicion == '3' or posicion == '4' or posicion == '5' or posicion == '6' or posicion == '7' or posicion == '8' or posicion == '9' or (tipo == 'float' and posicion=='.'):
            valor+=posicion
    if valor == '' or valor == ' ':
        valor = 0 
    if tipo == 'int':
        return int(valor)
    else:
        return float(valor) 
def escribir(mensaje,tipo):
    while True:
        texto = input(mensaje)
        valido = True
        for caracter in texto:
            if caracter == '[' or caracter == ']':
                valido = False
        if tipo != 'string' and tipo != 'str': 
            texto = filtrar(texto,tipo)
        if valido:
            break
    return '['+str(texto)+']'
def modificar(objeto,hasta_posicion,valor):
    prePosicion = '';postPosicion = '';posicion = 0
    for indice in range(len(objeto)):
        caracter_actual = objeto[indice]
        if caracter_actual == '[':
            posicion+=1
        if posicion < int(hasta_posicion):
            prePosicion += caracter_actual
        if posicion > hasta_posicion:
            postPosicion += caracter_actual
    return prePosicion + '[' + str(valor) + ']' + postPosicion
def menu_transaccion(cuenta):
    menus('Transacciones',True,True,True);menus('[1] Consultar saldo');menus('[2] Retirar dinero');menus('[3] Depositar dinero',border_bottom=True);  
    global saldos, total_depositado,total_retirado 
    opcion = int(input('|> Escriba su opcion: '))
    match opcion:
        case 1: 
            print(f"|> Saldo actual: {leer(saldos,cuenta)}")
        case 2: 
            retiro = filtrar(input('Introduzca el monto a retirar: '),'float')
            if retiro <= cajero_saldo:
                saldos = modificar(saldos,cuenta,retiro)
                total_retirado += retiro
                print('|> saldo retirado') 
            else:
                print('Saldo en le cajero insuficiente')
        case 3: 
            deposito = filtrar(input('Introduzca el monto a depositar: '),'float')
            saldos = modificar(saldos,cuenta,deposito)
            total_depositado += deposito
            print('|> saldo retirado') 
        case _: print('|***opcion no valida')
while True:
    menus('Menu principal',True,True); menus('Opciones',True,True,True); menus('[1] Recarga de efectivo cajero'); menus('[2] Registro de nuevo cliente'); menus('[3] Crear nuevo NIP');menus('[4] Realizar transacción en cajero');menus('[5] Reporte transacciones');menus('[6] Salir',border_bottom=True);
    opcion = filtrar(input('|> Escriba su opcion: '),'int');
    match opcion:    
        case 1: 
            cajero_saldo += filtrar(input('|> Introduce la cantidad a recargar en el cajero: '),'float')
            print(f'|> recarga de exitosa, saldo actual del cajero es: {cajero_saldo} ')
        case 2:
            if total_cuentas < 5:
                while True: 
                    num = filtrar(input('|> Introduce tu numero de cuenta: '),'int')
                    if buscar(cuentas, num) == False:
                        cuentas += '['+str(num)+']' 
                        break
                while True:
                    nip = filtrar(input('|> introduce tu NIP: '),'int')
                    nip2 = filtrar(input('|> Confirma tu NIP: '),'int')
                    if(nip == nip2 and len(str(nip)) == 4):
                        nips += '['+str(nip)+']'    
                        break
                    else:
                        print('|*** invalido o no coincide')
                nombres += escribir('|> Introduce tu nombre: ','str')
                saldos += escribir('|> Introduce tu saldo: ','float')
                total_cuentas+=1
            else:
                print('|*** Limite de cuentas alcanzadas')
        case 3:
            num = filtrar(input('|> Introduce tu numero de cuenta: '),'int')
            if buscar(cuentas, num):
                viejo_nip = filtrar(input('|> Introduce tu NIP anterior: '),'int')
                if int(leer(nips,buscar(cuentas, num,retornar_posicion=True))) == int(viejo_nip):
                    while True:
                        nip = filtrar(input('|> Introduce tu nuevo NIP: '),'int')
                        nip2 = filtrar(input('|> Confirma tu NIP: '),'int')
                        if(nip == nip2 and len(str(nip)) == 4):
                            nips = modificar(nips,buscar(cuentas,num,retornar_posicion=True),nip)
                            cambios_de_nip+=1
                            break
                        else: 
                            print('|*** NIP no coincide ')   
                else: 
                    print('|*** NIP no valido ')
            else: 
                print('|*** Cuenta no valido ')
        case 4:
            num = filtrar(input('|> Introduce tu numero de cuenta: '),'int')
            print(int(leer(nips,buscar(cuentas, num,retornar_posicion=True))))
            if buscar(cuentas, num):
                nip = filtrar(input('|> Introduce tu NIP: '),'int')
                if int(leer(nips,buscar(cuentas, num,retornar_posicion=True))) == nip:
                    menu_transaccion(buscar(cuentas, num,retornar_posicion=True))
                else: print('|> NIP no valida')
            else: print('|> Cuenta no valida')
        case 5:
            print(f'|> Total retirado: ${total_retirado} \n Total depositado: ${total_depositado} \n Total de cambios de nip: ${cambios_de_nip}')
        case 6:
            break
        case _:
            print('|*** Opcion no valida ')
