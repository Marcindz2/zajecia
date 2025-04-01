# Dziedziczenie klas. Klasa Animal ma zawierać atrybuty takie jak name, 
# age, sex oraz metodę sound(). Klasy Dog, Cat oraz Fox dziedziczą po 
# klasie Animal oraz nadpisują funkcje sound() odpowiednimi dźwiękami, 
# dodatkowo klasy Dog oraz Cat posiadają atrybut breed.
from collections import Counter
import random 
import string
class Animal:
    def __init__(self, name, age, sex):
        self.name=name
        self.age = age
        self.sex = sex
    def sound(self):
        return "dzwiek"

class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed=breed
    def sound(self):
        return "mrrrr miał"

class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed=breed
    def sound(self):
        return "szczek szczek"

class Fox(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def sound(self):
        return "szczekanie podobnie jak psy, ale głosem krótkim, o wyższej tonacji"


if __name__ == '__main__':
    kot=Cat("Furia",1.5,"female","krotkowlosa")
    pies=Dog("Azor",3,"male","bamblador")
    lis=Fox("Radek",23,"male")
    
    print(f"{kot.sound()}")
    print(f"{pies.sound()}")
    print(f"{lis.sound()}")