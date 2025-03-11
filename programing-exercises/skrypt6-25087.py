# Napisz program, który tworzy słownik o nazwie zawierającej Twój numer albumu.
# Kluczami powinny być liczby od 10 do 20, a wartościami pseudolosowe łańcuch znaków o długości 8.
# Hint: skorzystaj z modułów string i random.

import random 
import string
def ciag():
    znaki=string.ascii_letters
    temp=""
    for i in range(8):
        temp+=random.choice(znaki)
    return temp

def sposob1():
    slownik25087={i:ciag() for i in range(10,21)}
    return slownik25087

if __name__ == '__main__':
    
    print(f"odpowiedz to: {sposob1()}")
   