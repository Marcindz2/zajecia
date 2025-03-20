# Odwrócić sentencję podaną przez użytkownika.
def odwroc(word: str) -> str:
    
    return word[::-1]


if __name__ == '__main__':
    sentencja = input('Podaj ciąg ')
    print(f"odwrocony ciągu wejściowego to: {odwroc(sentencja)}")