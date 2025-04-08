# Należy wykorzystać plik wordlist_10000.txt i stworzyć funkcję 
# wyszukującą najdłuższy wyraz w tym pliku oraz drugą funkcję, 
# która wyszuka wyrazy o długości 10.
import random 
import string


    


def plik():
    with open("wordlist_10000.txt",'r') as file:
        longest=["",0]
        tenlong=[]
        for line in file:
            word=line.strip()
            length=len(word)
            if(length==10):
                tenlong.append(word)
            if(length>longest[1]):
                longest[0]=word
                longest[1]=length
        print(f"wyrazy o 10 znakach: {tenlong}, najdluzszy wyraz {longest}")
            


if __name__ == '__main__':
    plik()