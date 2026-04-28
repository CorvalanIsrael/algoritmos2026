
def factorial_recursivo (n):
    if n == 0:
        return 1
    else:
        return n *factorial_recursivo (n-1)
    
def factorial_iterativo (n):
    result = 1
    for i in range (1, n+1):
        result *= i

    return result

input_num = int (input ("Ingrese un numero: "))
print(factorial_iterativo(input_num))
