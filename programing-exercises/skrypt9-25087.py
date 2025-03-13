# Stwórz klasy Vehicle i Car z polami nazwa, rok_produkcji i przebieg 
# oraz metodami is_old() i is_long_mileage(). Stwórz po jednym obiekcie 
# dla każdej z klas oraz trzeci obiekt, gdzie klasa Car dziedziczy 
# z klasy Vehicle. Dla każdego z obiektów wywołaj obie metody, 
# co najmniej raz użyj dekoratora @property w każdym z trzech przypadków.

from collections import Counter
import random 
import string

class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    @property
    def is_old(self):
        current_year = 2025
        return current_year - self.rok_produkcji > 10

    @property
    def is_long_mileage(self):
        return self.przebieg > 200000
    
class Car:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    @property
    def is_old(self):
        current_year = 2025
        return current_year - self.rok_produkcji > 15

    @property
    def is_long_mileage(self):
        return self.przebieg > 100000
    
class Car2(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg,marka):
        super().__init__(nazwa, rok_produkcji, przebieg)
        self.marka=marka
    @property
    def is_old(self):
        current_year = 2025
        return current_year - self.rok_produkcji > 4
if __name__ == '__main__':
    vehicle = Vehicle("traktor",1999,30000)
    car=Car("BMW 3", 2005, 220000,)
    car2=Car2("BMW 3", 2022, 50000, "BMW")
    print(f"Vehicle - is_old: {vehicle.is_old}, is_long_mileage: {vehicle.is_long_mileage}")
    print(f"car - is_old: {car.is_old}, is_long_mileage: {car.is_long_mileage}")
    print(f"car2 - is_old: {car2.is_old}, is_long_mileage: {car2.is_long_mileage}")
   