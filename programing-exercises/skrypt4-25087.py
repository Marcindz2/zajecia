# Napisz program, który szuka określonego ciągu znaków w łańcuchu znakowym i zwraca indeksy wszystkich wystąpień ciągu lub -1, gdy nie ma takiego ciągu.
# Hint: skorzystaj z funkcji split().


# Napisz program, który szuka określonego ciągu znaków w łańcuchu znakowym i zwraca indeks pierwszego wystąpienia ciągu lub -1, gdy nie ma takiego ciągu.
# Hint: skorzystaj z funkcji find().

def szukanie(ciag1,ciag2 )->str:
    indeksy=[]
    podzial=ciag1.split(ciag2)
    print(podzial)
    print(len(podzial)-1)
    indeks = 0
    for i in range(len(podzial) - 1):  
        indeks += len(podzial[i])  
        indeksy.append(indeks)  
        indeks += len(podzial) 
    return indeksy

if __name__ == '__main__':
    pelny = 'piotr karol adam karol adam karol'#input('podaj pelny ciag: ')
    szukany = 'adam'#input('podaj szukany ciag: ')

    
    print(f"odpowiedz to: {szukanie(pelny, szukany)}")