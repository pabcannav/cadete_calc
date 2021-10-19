'''
Created on 12 oct 2021

@author: PCN
'''

def ca1(numerobinario):
    '''
    Entrada: Numero binario
    Salida: Complemento a1 de ese numero en formato string
    '''
    #Primero me aseguro de que sea una cadena de texto
    num = str(numerobinario)
    # Lo paso a lista para separar sus elementos
    num = list(num)
    numca1 = []
    for x in num:
        if x == "1":
            numca1.append("0")
        elif x== "0":
            numca1.append("1")
    return "".join(numca1)
def ca2(numerobinario):
    '''
    Entrada: Numero binario
    Salida: Complemento a2 de ese numero en formato string
    '''
    # Aprovechamos la funcion anterior y le sumamos 1 para hacer el Ca2.
    suma = int(ca1(numerobinario),2) + int("1",2)
    numca2 = bin(suma)
    numca2 = numca2[2:]
    if len(ca1(numerobinario)) != len(numca2):
        listaaux = list(str(numca2))
        while len(listaaux) != len(ca1(numerobinario)):
            listaaux.insert(0, "0")
        retorno = "".join(listaaux)
        return retorno
    else:
        return str(numca2)


