# Napisać funkcję tworzącą plik pc.csv. Pierwszy wiersz ma zawierać nazwy 
# kolumn: pc_name, ip. Nazwy komputerów mają zaczynać się literą P 
# oraz 4 oktetem adresu ip. 
# Adresy zaczynają się od 172.30.2.1 do 172.30.2.100. 
# Plik csv ma być rozdzielany przecinkami.

import csv

def plik():
    
    with open("pc.csv",'w',newline="") as file:
        writer=csv.writer(file)
        writer.writerow(['pc_name','ip'])
        for pc in range(1,101):
            name="p"+str(pc)
            ip="172.30.2."+str(pc)
            writer.writerow([name,ip])

if __name__ == '__main__':
    plik()