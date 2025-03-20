# Napisz prostą funkcję o nazwie potega(), przyjmującą jeden argument, 
# podnoszącą podaną liczbę do trzeciej potęgi.
import math
def potega(a):
    return math.pow(a,3)


if __name__ == '__main__':
    a=input("podaj liczbe: ")
    print(f"liczba podniesiona do 3 potegi \n {potega(float(a))}")
    
