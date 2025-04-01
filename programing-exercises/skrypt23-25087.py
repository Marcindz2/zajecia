# Za pomocą pętli stworzyć 1000 losowych 6 znakowych wyrazów
#  [A-Z][a-z][0-9] i zapisać je do pliku passwords.txt.
import random 
import string

def plik():
    znaki=string.ascii_lowercase+string.ascii_uppercase+string.digits
    with open("password.txt",'w') as file:
        for j in range(1000):
            ciag1=""
            for i in range(6):
                ciag1+=random.choice(znaki)
            file.write(f"{ciag1}\n")


if __name__ == '__main__':
    plik()