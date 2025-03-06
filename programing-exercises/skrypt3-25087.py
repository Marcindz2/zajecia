# Napisz program, który szuka określonego ciągu znaków w łańcuchu znakowym i zwraca indeks pierwszego wystąpienia ciągu lub -1, gdy nie ma takiego ciągu.
# Hint: skorzystaj z funkcji find().

def szukanie(ciag1,ciag2 )->str:
    return ciag1.find(ciag2)

if __name__ == '__main__':
    pelny = input('podaj pelny ciag: ')
    szukany = input('podaj szukany ciag: ')

    
    print(f"odpowiedz to: {szukanie(pelny, szukany)}")