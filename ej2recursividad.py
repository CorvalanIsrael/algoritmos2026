#Implementar una función que calcule la suma de todos los números enteros comprendidos
#entre cero y un número entero positivo dado.

def suma_recursiva (n: int) -> int:
    if n == 0:
        return n
    else:
        return n + suma_recursiva(n - 1)
    
'''Implementar una función para calcular
 el producto de dos números enteros dados.'''
def producto_recursivo(n: int, m: int) -> int:
    '''el producto de dos numeros de forma recursiva'''
    if n==0 or m==0:
        return 0
    else:
       return producto_recursivo(n + n, m-1)

#ej 7 serie

def serie_h(n) -> float:
    if n == 1:
        return 1
    else:
        return 1/n + serie_h(n-1)

'''8) Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a siste-
ma binario.'''
'''
4/2 = 2 % 0
        2/2= 1->n % 0
            1/2= 0 % 1
module(n/2 )->n + module (n/2)

n
  
'''
def bin_converter(n: int) -> str:
    if n == 1:
        return "1"
    if n== 0:
        return "0"
    else:
        if n%2 == 0:
            return  bin_converter(n//2) +"0" 
        elif n%2 == 1:
            return  bin_converter(n//2) + "1"


def num_romano(n: int) -> str:
    if n == 0:
        return "" 
    elif n >= 10:
        return "X" + num_romano(n-10) 
    elif n == 9:
        return "IX" + num_romano(n-9)  
    elif n >= 5:
        return "V" + num_romano(n-5) 
    elif n == 4:
        return "IV" + num_romano(n-4) 
    elif n >=1  and n < 4:
        return "I" + num_romano(n-1)