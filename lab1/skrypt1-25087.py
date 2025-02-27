# Napisz program (na dwa sposoby), który sprawdza czy wczytany pojedynczy znak jest cyfrą lub nie. Jeśli wczytamy więcej znaków, należy wziąć tylko pierwszy.
# Hint: skorzystaj z funkcji isdigit() i isinstance().


# def palindrome(word: str) -> str:
#     """
#     Funkcja ma za zadanie odwrócić sentencję podaną przez użytkownika
#     :param word: wejściowy łańcuch znaków
#     :return: palindrom wejściowego łańcucha znaków
#     """
#     return word[::-1]


# if __name__ == '__main__':
#     sentencja = input('Podaj ciąg znaków: ')
#     print(f"Palindrom ciągu wejściowego to: {palindrome(sentencja)}")

def czyCyfra(word: str) -> str:
    if word[0].isdigit():
        odpowiedz = True
    else:
        odpowiedz = False
    return odpowiedz

def czyCyfra2(word: str) -> str:
    try:
        if isinstance(int(word[0]),int):
            odpowiedz = True
            
    except ValueError:
        odpowiedz=False
    return odpowiedz
        

if __name__ == '__main__':
    cin = input('Podaj znak: ')
    print(f"odpowiedz 1 sposobu to: {czyCyfra(cin)}")
    print(f"odpowiedz 2 sposobu to: {czyCyfra2(cin)}")