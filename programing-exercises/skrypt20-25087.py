# Prosta gra, program generuje losową liczbę od 1 do 100, użytkownik ma 
# odgadnąć liczbę, jeżeli nie trafi ma zostać wyświetlona podpowiedź czy 
# za duża czy za mała liczba.
import random


if __name__ == '__main__':
    a=0
    liczba=random.randint(1,100)
    while a!=liczba:
        try:
            a = float(input('Podaj liczbę: '))
        except ValueError:
            print("to nie liczba")
        if liczba>a:
            print('liczba jest wieksza')
        if liczba<a:
            print('liczba jest mniejsza')
    
    print(f"udało ci sie znalezc!! liczba to {liczba}")
    