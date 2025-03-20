# Używając pętli wyświetl liczby w przedziale od 1 do 100 
# podzielne przez 3 i 4 oraz podaj ich liczbę.
def liczby():
    array=[]
    for i in range(1,100):
        if i%3==0 and i%4==0:
            array.append(i)
    return array, len(array)


if __name__ == '__main__':
    
    print(f"liczby od 1 do 100 podzielne przez 3 i 4: \n {liczby()}")
    
