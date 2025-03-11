# Stwórz folder utils, a w nim plik 'obliczenia.py', w którym należy zaimplementować cztery wybrane funkcje matematyczne z modułu math.
# Następnie należy utworzyć plik skrypt7-nr_albumu.py i zaimportować w nim ww. funkcje do obliczeń na przykładowych wartościach.
from utils import obliczenia

if __name__ == '__main__':

    try:
        a = float(input('Podaj a: '))
        b = float(input('Podaj b: '))
    except ValueError:
        print("to nie liczby")
    
    print(f"wynik potegowania a do b to: {obliczenia.potegowanie(a,b)}")
    print(f"silnia a to: {obliczenia.silnia(int(a))}")
    print(f"silnia b to: {obliczenia.silnia(int(b))}")
    print(f"logarytm z a o podstawie b to: {obliczenia.logarytm(int(a),int(b))}")
    print(f"cos(b) to: {obliczenia.cosinus(int(b))}")
   