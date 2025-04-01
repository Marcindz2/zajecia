# Sprawdź czy wyraz bądź zdanie podane przez użytkownika jest palindromem.
def odwroc(word: str) -> str:
    
    return word[::-1]

def porownaj(word: str, drow:str) -> str:
    if word==drow:
        return True
    else:
        return False

if __name__ == '__main__':
    sentencja = input('Podaj ciąg ')
    print(f"odwrocony ciąg wejściowy to: {odwroc(sentencja)}")
    odwr=odwroc(sentencja)
    print(porownaj(sentencja,odwr))