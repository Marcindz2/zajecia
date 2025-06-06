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
    return all(znak.isdigit() for znak in word)

if __name__ == '__main__':
    cin = input('Podaj co najmniej dwa znaki: ')
    if len(cin)<2:
         cin = input('Podaj conajmniej dwa znaki: ')
    print(f"odpowiedz to: {czyCyfra(cin)}")
    
# Napisz program, który sprawdza czy wczytany łańcuch znakowy jest liczbą lub nie. Muszą być wczytane co najmniej dwa znaki.
# Hint: skorzystaj z funkcji all().