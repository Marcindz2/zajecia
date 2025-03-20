# Używając pętli wyświetl liczby w przedziale od 1 do 50 oprócz liczb 
# podzielnych przez 3.
def liczby():
    array=[]
    for i in range(1,51):
        if i%3!=0:
            array.append(i)
    return array


if __name__ == '__main__':
    
    print(f"liczby od 1 do 50 niepodzielne przez 3: \n {liczby()}")
    