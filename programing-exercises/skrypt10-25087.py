# Napisz program, który korzystająć z metody chr() wygeneruje łańcuch 
# znakowy z alfabetem, czyli 'abc....xyz'. Do pliku 
# alfabet1-numeralbumu.txt zapisz wygenerowany łańcuch znakowy, 
# a do pliku alfabet2-numeralbumu.txt zapisz litery z ww. łańcucha 
# znakowego, tylko że każda litera ma się znaleźć w osobnej linii w pliku.
# Hint: oprócz funkcji write() skorzystaj również z menadżera kontekstu 
# with, żeby nie zapomnieć o zamknięciu pliku.
def plik1():
    with open("alfabet1-25087.txt",'w') as file:
        ciag1=""
        for i in range(26):
            ciag1+=chr(65+i)
            ciag1+=" "
        file.write(f"{ciag1}")

def plik2():
    with open("alfabet2-25087.txt",'w') as file:
        ciag1=""
        for i in range(26):
            ciag1+=chr(65+i)
            file.write(f"{ciag1[i]}\n")


if __name__ == '__main__':
    plik1()
    plik2()