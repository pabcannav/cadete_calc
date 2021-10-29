from tablasdeverdad import funcion

'''
Lo mismo que con las tablas de verdad pero con los mapas de karnaugh,
los dibujos de los mapas no son lo mejor pero son una guia y demasiado
que me he puesto a dibujar con putos caracteres ASCII.

SE SIGUE DEFINIENDO LA FUNCIÓN EN tablasdeverdad.py
'''
def kmapa3var():
    listai = [bin(x)[2:] for x in range(0,8)]
    listaarreglada = []
    valf = []
    for x in listai:
        if len(x) != 3:
            aux= list(str(x))
            while len(aux) != 3:
                aux.insert(0, "0")
            listaarreglada.append("".join(aux))
        else:
            listaarreglada.append(x)
    for x in listaarreglada:
        valf.append(funcion(int(x[0]),int(x[1]),int(x[2])))
    print('''
       c \ ab
          \  00 01 11 10
           \ ________________
          0 | {a}| {c}| {e}| {g}|
          1 | {b}| {d}| {f}| {h}|
    '''.format(a=valf[0],b=valf[1],c=valf[2],d=valf[3],e=valf[6],f=valf[7],g=valf[4],h=valf[5]))
def kmapa4var():
    listai = [bin(x)[2:] for x in range(0,16)]
    listaarreglada = []
    valf = []
    for x in listai:
        if len(x) != 4:
            aux= list(str(x))
            while len(aux) != 4:
                aux.insert(0, "0")
            listaarreglada.append("".join(aux))
        else:
            listaarreglada.append(x)
    for x in listaarreglada:
        valf.append(funcion(int(x[0]),int(x[1]),int(x[2]),int(x[3])))
    print('''
      cd \ ab
          \  00  01  11  10
           \ ________________
         00 |{a}  |{e}  |{i}  |{m}  |
         01 |{b}  |{f}  |{j}  |{n}  |
         11 |{c}  |{g}  |{k}  |{p}  |
         10 |{d}  |{h}  |{l}  |{q}  |
    '''.format(a=valf[0],b=valf[1],c=valf[3],d=valf[2],e=valf[4],f=valf[5],g=valf[7],h=valf[6],i=valf[12],j=valf[13],k=valf[15],l=valf[14],m=valf[8],n=valf[9],p=valf[11],q=valf[10]))
def kmapa5var():
    listai = [bin(x)[2:] for x in range(0,32)]
    listaarreglada = []
    valf = []
    for x in listai:
        if len(x) != 5:
            aux= list(str(x))
            while len(aux) != 5:
                aux.insert(0, "0")
            listaarreglada.append("".join(aux))
        else:
            listaarreglada.append(x)
    for x in listaarreglada:
        valf.append(funcion(int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4])))
    print(f'''
      de \ abc
          \  000 001 011 010 110 111 101 100
           \ ______________________________________
         00 |{valf[0]}  |{valf[4]}  |{valf[12]}  |{valf[8]}  |{valf[24]}  |{valf[28]}  |{valf[20]}  |{valf[16]}  |
         01 |{valf[1]}  |{valf[5]}  |{valf[13]}  |{valf[9]}  |{valf[25]}  |{valf[29]}  |{valf[21]}  |{valf[17]}  |
         11 |{valf[3]}  |{valf[7]}  |{valf[15]}  |{valf[11]}  |{valf[27]}  |{valf[31]}  |{valf[23]}  |{valf[19]}  |
         10 |{valf[2]}  |{valf[6]}  |{valf[14]}  |{valf[10]}  |{valf[26]}  |{valf[30]}  |{valf[22]}  |{valf[18]}  |
    ''')
