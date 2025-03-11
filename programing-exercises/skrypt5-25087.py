# Napisz program (na dwa sposoby), który szuka pierwiastków liczb od 1 do 256 (włącznie) podzielnych bez reszty przez 2.
# Hint: skorzystaj z modułu math i z tzw. 'list comprehensions'.
import math

def sposob1():
    liczby= []
    for i in range(1,257):
        if (i % 2)==0:
            liczby.append(int(math.pow(i,2)))
    return liczby

def sposob2():
     liczby=[i*i for i in range(2,257,2)]
     return liczby

if __name__ == '__main__':
    
    print(f"odpowiedz to: {sposob1()}")
    print(f"druga odpowiedz: {sposob2()}")
    