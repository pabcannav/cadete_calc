# cadete_calc
Calculadora para la asignatura de Circuitos Electronicos Digitales

## Documentación de funciones
### cambiodebase.py
Basicamente en este script hay definidas varias funciones para facilitar los cambios de base, no hay mucho que
explicar.
### complementos.py
Incluye dos funciones para realizar las operaciones de complemento a1 y complemento a2
### operadoreslogicos.py
Implementacion de los operadores logicos en python, basicamente las funciones a tener en cuenta en este fichero son:
1. **AND**: Para el operador lógico AND existen las funciones de tand(a,b), tand3(a,b,c) (And de 3 entradas),
tand4(a,b,c,d) (And de 4 entradas) y tand5(a,b,c,d,e)
2. **OR**: Para el operador lógico OR existen las mismas funciones que en la and, tor(),tor3(),tor4(),tor5()
3. **NOT**: Para el operador lógico NOT existen dos funciones, tnot(a) que trabaja unicamente con TRUE O FALSE
y altnot(a) que trabaja con 0 y 1, este el ultimo es que usaremos en los generadores de funciones
4. **NAND**: Para el operador NAND --> tnand(),tnand3(),tnand4(),tnand5()
5. **NOR**: Para el operador NOR --> tnor(),tnor3(),tnor4(),tnor5()
6. **XOR**: Para el operador XOR --> txor(),txor3(),txor4(),txor5()
7. **XNOR**: Para el operador XNOR --> tnxor(),tnxor3(),tnxor4(),tnxor5()
### tablasdeverdad.py
Esta es una de las funciones más ultiles de la calculadora, en este fichero puedes definir una función de hasta
5 variables para imprimir su tabla de verdad. Es importante que dejéis el nombre de la función  como "funcion"
si no no os funcionará. Aquí algunos ejemplos de funciones que podeis definir:

def funcion(a,b)
    return tor(a,b)
    
def funcion(a,b,c):
    return txor(tand(a, b),c)
    
def funcion(a,b,c,d):
    return tor3(tnand(a,b),txor(b,c),tnxor(c,d))

def funcion(a,b,c,d,e)
    return tor4(a,tand3(b,altnot(c),d),e,altnot(e))
### gfunciones.py
Aquí en donde se genera la función definida en tablasdeverdad.py, ejemplos de lo que podéis hacer en este script:

print(funcion(1,0,1,1)) --> Para evaluar un valor concreto de la funcion.
tabladeverdad4variables --> Tabla de verdad si habeis definido una función de 4 variables.
## tests.py
Para realizar cualquier operacion importando los modulos de la calculadora