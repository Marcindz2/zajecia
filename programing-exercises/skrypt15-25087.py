# Używając pętli dodawaj do wcześniej zadeklarowanej tabeli liczby 
# z przedziału od 1 do 100, które są podzielne przez 3 lub podzielne 
# przez 5.
def liczby():
    array=[]
    for i in range(1,100):
        if i%3==0 or i%5==0:
            array.append(i)
    return array


if __name__ == '__main__':
    
    print(f"liczby od 1 do 100 podzielne przez 3 lub 5: \n {liczby()}")
    
