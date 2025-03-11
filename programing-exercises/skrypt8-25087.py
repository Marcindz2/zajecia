# Napisz program, który generuje losowy ciąg znaków o długości 100, a następnie utwórz słownik którego kluczami będą unikalne znaki występujące w ciągu, a wartościami liczba ich wystąpień w ciągu znakowym. Utwórz listę, której każdy element to krotka (tupla), zawierająca kolejny klucz z ww. słownika i odpowiadającą mu wartość liczbową.
# Hint: skorzystaj z modułu collections i klasy Counter().

from collections import Counter
import random 
import string
def ciag():
    znaki=string.ascii_lowercase
    temp=""
    for i in range(100):
        temp+=random.choice(znaki)
    #counter tworzy w pewnym sensie slownik 
    licznik=Counter(temp)
    
    znaki=list(licznik.keys())
    liczby=list(licznik.values())
    return znaki,liczby

def sposob1():
    klucze,wartosci=ciag()
    
    
    lista=list(zip(klucze,wartosci))
    return lista

if __name__ == '__main__':
    
    print(f"odpowiedz to: {sposob1()}")
   