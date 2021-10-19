'''
Created on 12 oct 2021

@author: PCN
'''
def conversor(num):
    '''
    Dado que python trabaja con valores booleanos
    true o false vamos a hacer una funcion muy 
    simple para hacer la conversion de un 1 a True
    y de 0 a false
    '''
    if num == 1:
        return True
    elif num == 0:
        return False
def deconversor(valorbol):
    '''
    Lo mismo que la anterior pero para que nos devuelva el 1 o el 0
    '''
    if valorbol == True:
        return 1
    elif valorbol == False:
        return 0
def tnot(valor):
    '''
    vamos a crear el not que va a ser necesario para las demas funciones
    teniendo en cuenta que nuestras puertas logicas van a operar con
    True o False y no con 0 o 1 este not trabajara con VALORES BOOLEANOS
    '''
    return not valor 
def altnot(valor):
    '''
    Este not por el contrario trabaja con los 0 y los 1, lo cual es interesante
    a la hora de generar funciones.
    '''
    if valor == 1:
        return 0
    if valor == 0:
        return 1
def tand(valor1,valor2):
    '''
    Vamos a hacer nuestro operador logico and para trabajar con 1 y 0
    '''
    a = conversor(valor1) and conversor(valor2)
    return deconversor(a)
def tor(valor1,valor2):
    a = conversor(valor1) or conversor(valor2)
    return deconversor(a)
def txor(valor1,valor2):
    '''
    Haremos la implementacion (a+b)*(a'+b')
    '''
    valor1, valor2 = conversor(valor1), conversor(valor2) 
    a = (valor1 or valor2) and (tnot(valor1) or tnot(valor2))
    return deconversor(a)
def tnand(valor1,valor2):
    '''
    Vamos a hacer una implementacion de la puerta Nand utilizando
    algunas funciones anteriores
    Parece un poco lio pero es sencillo, aplicamos primero la and,
    como el valor resultante es un 1 o un 0 usamos el conversor para
    pasarlo a un valor booleano para poder aplicar el not y luego usar
    el deconversor para obtener finalmente un 0 o un 1.
    '''
    return deconversor(tnot(conversor(tand(valor1, valor2))))
def tnor(valor1,valor2):
    return deconversor(tnot(conversor(tor(valor1, valor2))))
def tnxor(valor1,valor2):
    return deconversor(tnot(conversor(txor(valor1, valor2))))
def tand3(valor1,valor2,valor3):
    # Puerta And de 3 entradas
    return tand(tand(valor1, valor2),valor3)
def tand4(valor1,valor2,valor3,valor4):
    # Puerta And de 4 entradas
    return tand(tand3(valor1, valor2, valor3), valor4)
def tand5(valor1,valor2,valor3,valor4,valor5):
    # Puerta And de 5 entradas
    return tand(tand4(valor1, valor2, valor3, valor4), valor5)
def tor3(valor1,valor2,valor3):
    return tor(tor(valor1, valor2), valor3)
def tor4(valor1,valor2,valor3,valor4):
    return tor(tor3(valor1, valor2, valor3), valor4)
def tor5(valor1,valor2,valor3,valor4,valor5):
    return tor(tor4(valor1, valor2, valor3, valor4), valor5)
def tnand3(valor1,valor2,valor3):
    return altnot(tand3(valor1, valor2, valor3))
def tnand4(valor1,valor2,valor3,valor4):
    return altnot(tand4(valor1, valor2, valor3, valor4))
def tnand5(valor1,valor2,valor3,valor4,valor5):
    return altnot(tand5(valor1, valor2, valor3, valor4, valor5))
def txor3(valor1,valor2,valor3):
    return txor(txor(valor1, valor2), valor3)
def txor4(valor1,valor2,valor3,valor4):
    return txor(txor3(valor1, valor2, valor3), valor4)
def txor5(valor1,valor2,valor3,valor4,valor5):
    return txor(txor4(valor1, valor2, valor3, valor4), valor5)
def tnxor3(valor1,valor2,valor3):
    return altnot(txor3(valor1, valor2, valor3))
def tnxor4(valor1,valor2,valor3,valor4):
    return altnot(txor4(valor1, valor2, valor3, valor4))
def tnxor5(valor1,valor2,valor3,valor4,valor5):
    return altnot(txor5(valor1, valor2, valor3, valor4, valor5))