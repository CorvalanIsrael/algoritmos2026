# '''El problema de la mochila Jedi. Suponga que un Jedi 
# (Luke Skywalker, Obi-Wan Kenobi, Rey u 
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que 
# contiene muchos objetos. Implementar una función recursiva llamada
# “usar la fuerza” que le permita al Jedi “con 
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar 
# un sable de luz o que no 
# queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios
#  sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.'''

mochila = ["sable de luz", "comida", "agua", "baby-joda", "wookie", "Ar-turito"]

def usar_la_fuerza(mochila, count = 0) -> str:
    '''mochila:[] -> devuelve el sable de luz
   con ayuda de la fuerza el JEdi saca un elemento por vez de forma recursiva'''
    
    elem = mochila.pop()
    count += 1
    if elem == "sable de luz":
        print("el Jedi usando la fuerza encontro el sable de luz")
        return elem, count
    elif len(mochila) == 0:
        print("no queda nada mas en la mochila")
        return None
    else:
        return usar_la_fuerza(mochila, count)
    
sacado = []
sacado = usar_la_fuerza(mochila)

if sacado == None:
    print('mochila vacía (no se encontró el sable)')
else:
    print( f'el sable {sacado[0]} se ubtuvo luego de sacar {sacado[1]} objetos y la mcohila quedo con {mochila} objetos')
