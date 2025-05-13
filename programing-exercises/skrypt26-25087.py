# Za pomocą webscrappera pobrać wszystkie oferty domów z podanego 
# linku(https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing), 
# każda oferta ma być obiektem klasy Home, który posiada atrybuty takie 
# jak header_name, price, price_for_m2. Wszystkie obiekty zapisać do 
# słownika oraz do pliku home.csv.
import requests 
from bs4 import BeautifulSoup
import re
import csv
class home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name=header_name
        self.price = price
        self.price_for_m2 = price_for_m2

def strona(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    hiperlacza=[]
    if response.status_code == 200:
        parse = BeautifulSoup(response.text, 'html.parser')
        
        articles = parse.find_all('article', attrs={'data-cy': 'listing-item'})
        
        for article in articles:
            nazwa = article.find('p', class_='css-u3orbr e1g5xnx10')
            nazwatext=nazwa.text
            #print(nazwatext)
            cena=article.find('span',class_="css-2bt9f1 evk7nst0") 
            cenatext=cena.text
            #print(f"cena to: {cenatext} zł")
            parametry=article.find('dl', class_="css-9q2yy4 eyjpr0t1")
            parametrytext=parametry.text
            result=re.split(r'Liczba pokoi|\s+pokojePowierzchnia|\s+m²Cena za metr kwadratowy|\s+zł/m²Piętro',parametrytext)
            #print(f'   ile pokoi: {result[1]} powierzchnia: {result[2]} cena za metr: {result[3]}')
            dom=home(nazwatext,cenatext,result[3])
            obiekty_home.append(dom)
    else:
        print(f"blad: {response.status_code}")

def plik(homes):
    with open("home.csv",'w',newline="", encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(['name','price','price/m2'])
        for home in homes:
            name=home.header_name
            price=home.price
            pricem2=home.price_for_m2
            writer.writerow([name,price])


if __name__ == '__main__':
    obiekty_home=[]
    # strona('https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing')
    strona('https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing&by=LATEST&direction=ASC')
    plik(obiekty_home)
    #for home in obiekty_home:
        #print(f" nazwa: {home.header_name}, cena: {home.price},   cena za metr: {home.price_for_m2}")




