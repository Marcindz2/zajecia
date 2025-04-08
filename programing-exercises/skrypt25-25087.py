# Za pomocą pakietu do web-scrappingu, np.beautifulsoup lub jsoup, 
# zapisać do tablicy wszystkie hiperłącza występujące na wybranej 
# przez siebie stronie.
import requests 
from bs4 import BeautifulSoup


def strona(url):
    response=requests.get(url)
    hiperlacza=[]
    if response.status_code == 200:
        parse = BeautifulSoup(response.text, 'html.parser')
        links = parse.find_all('a')
        for link in links:
            hiperlacza.append(link.get('href'))
        print(hiperlacza)
    else:
        print(f"blad: {response.status_code}")

if __name__ == '__main__':
    strona('https://www.plemiona.pl/')