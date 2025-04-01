# Stworzyć plik funkcje.py, w którym należy zaimplementować funkcję: 
# dodawanie, odejmowanie, dzielenie, mnożenie oraz modulo. 
# W pliku main.py zaimportować plik funkcje.py i wykorzystać 
# zaimportowane funkcje na przykładowych wartościach.
from utils import funkcje
    

    
if __name__ == '__main__':
    try:
        a = float(input('Podaj a: '))
        b = float(input('Podaj b: '))
    except ValueError:
        print("to nie liczby")

    print(f"wynik dodawania to: {funkcje.dodawanie(a,b)}")
    print(f"wynik odejmowania to: {funkcje.odejmowanie(a,b)}")
    print(f"wynik mnozenia to:{funkcje.mnozenie(a,b)}")
    if funkcje.dzielenie(a,b)!=False:
        print(f"wynik dzielenia to: {funkcje.dzielenie(a,b)}")
    print(f"wynik modulo to:{funkcje.modulo(a,b)}")
   