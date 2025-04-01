# Stworzyć plik funkcje.py, w którym należy zaimplementować funkcję: 
# dodawanie, odejmowanie, dzielenie, mnożenie oraz modulo. 
# W pliku main.py zaimportować plik funkcje.py i wykorzystać 
# zaimportowane funkcje na przykładowych wartościach.

import math

def dodawanie(a,b):
    return a+b

def dzielenie(a,b):
    if b==0:
        print("nie mozna dzielic przez zero")
        return False
    else:
        return a/b 

def odejmowanie(a,b):
    return a-b

def mnozenie(a,b):
    return a*b
def modulo(a,b):
    if b==0:
        print("nie mozna dzielic przez zero")
        return False
    else:
        return a%b
    