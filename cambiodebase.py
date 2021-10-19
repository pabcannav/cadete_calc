'''
Created on 13 oct 2021

@author: PCN
'''
# Cambios de base soportados hasta base 16
def decimalabinario(valor):
    a = bin(valor)
    return a[2:]
def binarioadecimal(valor):
    a = int(str(valor),2)
    return a
def decimalaoctal(valor):
    a = oct(valor)
    return a[2:]
def decimalahexadecimal(valor):
    a = hex(valor)
    return a[2:]
def hexadecimaladecimal(valor):
    a = int(str(valor),16)
    return a
def octaladecimal(valor):
    a = int(str(valor),8)
    return a
def decimalacualquierbase(valor,base):
    cociente = valor
    aux = []
    while cociente>0:
        resto = cociente%base
        cociente = cociente//base
        aux.append(str(resto))
    aux.reverse()
    return "".join(aux)
def cualquierbaseadecimal(valor,base):
    a = int(str(valor),base)
    return a
