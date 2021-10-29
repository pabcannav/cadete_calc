'''
Created on 12 oct 2021

@author: PCN
'''

from operadoreslogicos import *
#################################################
################################################
'''
En este script esta es la unica parte a modificar,
es importante que dejeis el nombre como "funcion"
si no no funcionara el script, podeis definir hasta 5 variables
hay algunas funciones comentadas para que sirvan de ejemplo
'''
'''
def funcion(a,b)
    return tor(a,b)
    
def funcion(a,b,c):
    return txor(tand(a, b),c)
    
def funcion(a,b,c,d):
    return tor(txor(a,b),tnand(c,d))

def funcion(a,b,c,d,e)
    return tor(tor(tand(a,b),tor(c,d)),e)
'''
def funcion(a,b,c):
    return tand3(a,b,c)
################################################
#################################################
def tabladeverdad4variables():
    dicc = dict()
    listai = [bin(x)[2:] for x in range(0,16)]
    listaarreglada = []
    for x in listai:
        if len(x) != 4:
            aux= list(str(x))
            while len(aux) != 4:
                aux.insert(0, "0")
            listaarreglada.append("".join(aux))
        else:
            listaarreglada.append(x)
    for x in listaarreglada:
        dicc[x] = funcion(int(x[0]),int(x[1]),int(x[2]),int(x[3]))
    for p in dicc:
        print("{} -> {} || {}".format(int(p,2),p,dicc[p]))
def tabladeverdad5variables():
    dicc = dict()
    listai = [bin(x)[2:] for x in range(0,32)]
    listaarreglada = []
    for x in listai:
        if len(x) != 5:
            aux= list(str(x))
            while len(aux) != 5:
                aux.insert(0, "0")
            listaarreglada.append("".join(aux))
        else:
            listaarreglada.append(x)
    for x in listaarreglada:
        dicc[x] = funcion(int(x[0]),int(x[1]),int(x[2]),int(x[3],int(x[4])))
    for p in dicc:
        print("{} -> {} || {}".format(int(p,2),p,dicc[p]))
def tabladeverdad3variables():
    dicc = dict()
    listai = [bin(x)[2:] for x in range(0,8)]
    listaarreglada = []
    for x in listai:
        if len(x) != 3:
            aux= list(str(x))
            while len(aux) != 3:
                aux.insert(0, "0")
            listaarreglada.append("".join(aux))
        else:
            listaarreglada.append(x)
    for x in listaarreglada:
        dicc[x] = funcion(int(x[0]),int(x[1]),int(x[2]))
    for p in dicc:
        print("{} -> {} || {}".format(int(p,2),p,dicc[p]))
def tabladeverdad2variables():
    dicc = dict()
    listai = [bin(x)[2:] for x in range(0,4)]
    listaarreglada = []
    for x in listai:
        if len(x) != 2:
            aux= list(str(x))
            while len(aux) != 2:
                aux.insert(0, "0")
            listaarreglada.append("".join(aux))
        else:
            listaarreglada.append(x)
    for x in listaarreglada:
        dicc[x] = funcion(int(x[0]),int(x[1]))
    for p in dicc:
        print("{} -> {} || {}".format(int(p,2),p,dicc[p]))
