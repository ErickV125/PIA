usuario_1_num_cuenta = 0;usuario_2_num_cuenta = 0;usuario_3_num_cuenta = 0;usuario_4_num_cuenta = 0;usuario_5_num_cuenta = 0
usuario_1_nombre = '';usuario_2_nombre = '';usuario_3_nombre = '';usuario_4_nombre = '';usuario_5_nombre = ''
usuario_1_saldo = 0;usuario_2_saldo = 0;usuario_3_saldo = 0;usuario_4_saldo = 0;usuario_5_saldo = 0
usuario_1_nip = '';usuario_2_nip = '';usuario_3_nip = '';usuario_4_nip = '';usuario_5_nip = ''
cajero_saldo = 1000;total_depositado = 0; total_retirado = 0; cambios_de_nip = 0
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

def fcuenta():
    while True: 
        num = int(input('Introduce el numero de cuenta: '))
        if(procesar_entrada(False,num,usuario_1_num_cuenta) != 0 or procesar_entrada(False,num,usuario_2_num_cuenta) != 0 or procesar_entrada(False,num,usuario_3_num_cuenta) != 0 or procesar_entrada(False,num,usuario_4_num_cuenta) != 0 or procesar_entrada(False,num,usuario_5_num_cuenta) != 0):
            return num
def fnip():
    while True: 
        nip = int(input('Introduce el NIP: '))
        nip2 = int(input('Confirme su NIP: '))
        if(nip == nip2):
            return nip
        else:
            print('NIP no coincide, intente de nuevo')
def fsaldo(mensaje,saldo = 0): 
    if(saldo > 0):
        return saldo
    else:        
        return float(input(mensaje))
            
def procesar_entrada(interactivo,parametro=False,cuenta=False,nip=False,saldo=False,mensaje = '',nuevo_saldo = 0):
    match interactivo:
        case True:
            if cuenta:
                return fcuenta()
            elif nip :
                return fnip()
            elif saldo:
                return fsaldo(mensaje,nuevo_saldo)
        case False:
            if cuenta==parametro:
                return cuenta
            elif nip==parametro:
                return nip
                  
def configuracion_usuario(num = -1,retornar_nip = False, modificar = False, cambiar_nip = False, cambiar_saldo = False, retornar_saldo = False,retornar_cuenta = False,mensaje_saldo = '',salida_err = '',nuevo_saldo=0):
    global usuario_1_num_cuenta, usuario_2_num_cuenta,usuario_3_num_cuenta,usuario_4_num_cuenta,usuario_5_num_cuenta
    global usuario_1_nombre, usuario_2_nombre, usuario_3_nombre, usuario_4_nombre, usuario_5_nombre
    global usuario_1_saldo, usuario_2_saldo, usuario_3_saldo, usuario_4_saldo, usuario_5_saldo
    global usuario_1_nip, usuario_2_nip, usuario_3_nip, usuario_4_nip, usuario_5_nip
    
    if (usuario_1_num_cuenta==0 and modificar) or procesar_entrada(interactivo=False,cuenta=usuario_1_num_cuenta,parametro=num) == num:
        if modificar == True:
            usuario_1_num_cuenta = procesar_entrada(True,cuenta=True)
            usuario_1_nombre = input('Introduzca su nombre: ')
        if cambiar_nip: usuario_1_nip = procesar_entrada(True,nip=True)
        if cambiar_saldo: usuario_1_saldo += procesar_entrada(True,saldo=True,mensaje=mensaje_saldo,nuevo_saldo=nuevo_saldo)
        if retornar_saldo: return usuario_1_saldo
        if retornar_cuenta: return usuario_1_num_cuenta
        if retornar_nip: return usuario_1_nip
        
    elif (usuario_2_num_cuenta==0 and modificar) or procesar_entrada(interactivo=False,cuenta=usuario_2_num_cuenta,parametro=num) == num:
        if modificar == True:
            usuario_2_num_cuenta = procesar_entrada(True,cuenta=True)
            usuario_2_nombre = input('Introduzca su nombre: ')
        if cambiar_nip: usuario_2_nip = procesar_entrada(True,nip=True)
        if cambiar_saldo: usuario_2_saldo += procesar_entrada(True,saldo=True,mensaje=mensaje_saldo,nuevo_saldo=nuevo_saldo)
        if retornar_saldo: return usuario_2_saldo
        if retornar_cuenta: return usuario_2_num_cuenta
        if retornar_nip: return usuario_2_nip

    elif (usuario_3_num_cuenta==0 and modificar) or procesar_entrada(interactivo=False,cuenta=usuario_3_num_cuenta,parametro=num) == num:
        if modificar == True:
            usuario_3_num_cuenta = procesar_entrada(True,cuenta=True)
            usuario_3_nombre = input('Introduzca su nombre: ')
        if cambiar_nip: usuario_3_nip = procesar_entrada(True,nip=True)
        if cambiar_saldo: usuario_3_saldo += procesar_entrada(True,saldo=True,mensaje=mensaje_saldo,nuevo_saldo=nuevo_saldo)
        if retornar_saldo: return usuario_3_saldo
        if retornar_cuenta: return usuario_3_num_cuenta
        if retornar_nip: return usuario_3_nip

    elif (usuario_4_num_cuenta==0 and modificar) or procesar_entrada(interactivo=False,cuenta=usuario_4_num_cuenta,parametro=num) == num:
        if modificar == True:
            usuario_4_num_cuenta = procesar_entrada(True,cuenta=True)
            usuario_4_nombre = input('Introduzca su nombre: ')
        if cambiar_nip: usuario_4_nip = procesar_entrada(True,nip=True)
        if cambiar_saldo: usuario_4_saldo += procesar_entrada(True,saldo=True,mensaje=mensaje_saldo,nuevo_saldo=nuevo_saldo)
        if retornar_saldo: return usuario_4_saldo
        if retornar_cuenta: return usuario_4_num_cuenta
        if retornar_nip: return usuario_4_nip

    elif (usuario_5_num_cuenta==0 and modificar) or procesar_entrada(interactivo=False,cuenta=usuario_5_num_cuenta,parametro=num) == num:
        if modificar == True:
            usuario_5_num_cuenta = procesar_entrada(True,cuenta=True)
            usuario_5_nombre = input('Introduzca su nombre: ')
        if cambiar_nip: usuario_5_nip = procesar_entrada(True,nip=True)
        if cambiar_saldo: usuario_5_saldo += procesar_entrada(True,saldo=True,mensaje=mensaje_saldo,nuevo_saldo=nuevo_saldo)
        if retornar_saldo: return usuario_5_saldo
        if retornar_cuenta: return usuario_5_num_cuenta
        if retornar_nip: return usuario_5_nip
    else:
        print(salida_err)

def recarga():
    global cajero_saldo
    while True:
        monto = int(input('Introduce el monto a recargar: '))
        if(monto >= 0):
            cajero_saldo+=monto
            break
        else:
            print('Monto introducido no valido')
            
def consultar_saldo(num):
    print('Saldo disponible: $',configuracion_usuario(num,retornar_saldo=True))
    
def retirar(num):
    global total_retirado, cajero_saldo
    while True:
        while True:
            retiro_actual = int(input('Introduce el monto a retirar: ')) 
            if retiro_actual > 0:
                break 
        saldo = configuracion_usuario(num,retornar_saldo=True)
        if retiro_actual > cajero_saldo:
            print('Fondos insuficientes en el cajero para completar la transaccion, por favor intentar con un monto menor o en otra sucursal')
        elif(retiro_actual <= saldo ):
            configuracion_usuario(num,cambiar_saldo=True,nuevo_saldo=(retiro_actual * -1))
            total_retirado+= retiro_actual
            cajero_saldo-=retiro_actual
        else:
            print('Fondos insufucientes en la cuenta')

def depositar(num):
    global total_depositado
    while True:
        deposito = float(input('Introduzca el saldo a depositar'))
        configuracion_usuario(num,cambiar_saldo=True,nuevo_saldo=deposito)
        total_depositado+= deposito 
        

def menu_transaccion(num):
    menus('Transacciones',True,True,True)   
    menus('[1] Consultar saldo')   
    menus('[2] Retirar dinero')   
    menus('[3] Depositar dinero',border_bottom=True)   
    opcion = int(input('Escriba su opcion: '))
    match opcion:
        case 1: consultar_saldo(num)
        case 2: retirar(num)
        case 3: depositar(num)
        case _: print('opcion no valida')
            
def reporte_transacciones():
    
    return False

while True:
    menus('Menu principal',True,True)   
    menus('Opciones',True,True,True)   
    menus('[1] Recarga de efectivo cajero')   
    menus('[2] Registro de nuevo cliente')   
    menus('[3] Crear nuevo NIP')   
    menus('[4] Realizar transacción en cajero')   
    menus('[5] Reporte transacciones')
    menus('[6] Salir',border_bottom=True)
    opcion = input('Escriba su opcion: ')
    match opcion:    
        case '1':
            recarga()
        case '2':
            configuracion_usuario(modificar=True,cambiar_nip=True,cambiar_saldo=True,mensaje_saldo='introduce tu saldo inicial: ',salida_err='limite de usuarios alcanzado')
        case '3':
            cuenta = int(input('Introduce el numero de cuenta: '))
            if configuracion_usuario(cuenta,retornar_cuenta=True) == cuenta:
                antiguo_nip = int(input('Introduce el nip antiguo: '))
                if configuracion_usuario(cuenta,retornar_nip=True) == antiguo_nip:
                    configuracion_usuario(cuenta,cambiar_nip=True)
                    cambios_de_nip+=1
                else: 
                    print('NIP ingresado no es valido')
            else: 
                print('Cuenta ingresada no valida')
        case '4':
            num_cuenta = int(input('Introduzca su numero de cuenta: '))
            if configuracion_usuario(num_cuenta,retornar_cuenta=True)==num_cuenta : 
                if configuracion_usuario(num_cuenta,retornar_nip=True) == int(input('Introduzca su nip: ')):
                    menu_transaccion(num_cuenta)
                else:
                    print('NIP no valida') 
            else:
                print('Cuenta no valida') 
        case '5':
             print('no hace na')

        case '6':
            break
        case _:
            print('Opcion no valida')
            
while True:
    menus('Menu principal',True,True); menus('Opciones',True,True,True); 
    menus('[1] Recarga de efectivo cajero'); 
    menus('[2] Registro de nuevo cliente'); 
    menus('[3] Crear nuevo NIP');
    menus('[4] Realizar transacción en cajero');
    menus('[5] Reporte transacciones');
    menus('[6] Salir',border_bottom=True);opcion = filtrar(input('Escriba su opcion: '),'int');
    match opcion:    
        case 1: 
            cajero_saldo += filtrar(input('Introduce la cantidad a recargar en el cajero: '),'float')
            print(f'recarga de exitosa, saldo actual del cajero es: {cajero_saldo} ')
        case 2:
            if total_cuentas < 5:
                while True: 
                    num = filtrar(input('Introduce tu numero de cuenta: '),'int')
                    print (buscar(cuentas, num))
                    if buscar(cuentas, num) == False:
                        cuentas += '['+str(num)+']' 
                        break
                while True:
                    nip = filtrar(input('introduce tu NIP: '),'int')
                    nip2 = filtrar(input('confirma tu NIP: '),'int')
                    if(nip == nip2 and len(str(nip)) == 4):
                        nips += '['+str(nip)+']'    
                        break
                nombres += escribir('Introduce tu nombre: ','str')
                saldos += escribir('Introduce tu saldo: ','float')
                total_cuentas+=1
            else:
                print('Limite de cuentas alcanzadas')
        case 3:
            num = filtrar(input('Introduce tu numero de cuenta: '),'int')
            if buscar(cuentas, num):
                viejo_nip = filtrar(input('Introduce tu NIP anterior: '),'int')
                if leer(nips,buscar(cuentas, num,retornar_posicion=True)) == viejo_nip:
                    while True:
                        nip = filtrar(input('introduce tu NIP'),'int')
                        nip2 = filtrar(input('confirma tu NIP'),'int')
                        if(nip == nip2 and len(nip) == 4):
                            nips = modificar(nips,leer(nips,buscar(cuentas, num,retornar_posicion=True)),nip)
                            cambios_de_nip+=1
                            break
                        else: print('NIP no coincide')   
                else: print('NIP no valido')
            else: print('Cuenta no valido')
        case 4:
            num = filtrar(input('Introduce tu numero de cuenta: '),'str')
            if buscar(cuentas, num):
                viejo_nip = filtrar(input('Introduce tu NIP: '),'int')
                if leer(nips,buscar(cuentas, num,retornar_posicion=True)) == viejo_nip:
                    menu_transaccion(leer(nips,buscar(cuentas, num,retornar_posicion=True)))
        case 5:
            print(f'Total retirado: ${total_retirado} \n Total depositado: ${total_depositado} \n Total de cambios de nip: ${cambios_de_nip}')
        case 6:
            break
        case _:
            print('Opcion no valida')
