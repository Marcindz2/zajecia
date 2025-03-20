# Zamienić wszystkie litery o na 0, e na 3, i na 1, 
# a na 4 w podanej przez użytkownika sentencji.
def wymiana(wej: str) -> str:
    return (wej.replace('o', '0').replace('e', '3').
            replace('i', '1').replace('a', '4'))


if __name__ == '__main__':
    wejscie = input('Podaj ciąg  ')
    print(f"ciąg po zamianie: {wymiana(wejscie)}")