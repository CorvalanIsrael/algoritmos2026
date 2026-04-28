'''Desarrollar una función que permita convertir un número romano en un número decimal'''

def num_romano(n: int) -> str:
    if n == 0:
        return "" 
    elif n >= 1000:
        return "M" + num_romano(n-1000)
    elif n >= 500:
        return "D" + num_romano(n-500)
    elif n >= 100: 
        return "C" + num_romano(n-100)
    elif n >= 50:
        return "L" + num_romano(n-50)
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
    
def num_decimal(s: str) -> int:
    num = 0
    for car in s:
        if car == ("i" or "I") and num=-=5:
            #s = s[:-1]
            num-=1
        #elif car == ("v" or "V") and num < 1:
            if car == "v" or car == "V":
                #s = s[:-1]
                num += 5
        if car == "x" or car == "X":
            #s = s[:-1]
            num += 10
    return num


print(num_decimal(input("ingrese un numero romano: ")))   
#print(num_romano(int(input("ingrese un numero decimal: "))))