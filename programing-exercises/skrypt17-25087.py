# Stwórz klasę o nazwie Dog, która będzie posiadała zmienne takie jak: 
# name, age, coat_color. Dodatkowo klasa posiada funkcje sound(), 
# po wywołaniu której wypisywany jest tekst: {name} is barking! 
# Stworzyć 3 obiekty klasy Dog.

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(f"{self.name} is barking!\n")
    

    
if __name__ == '__main__':
    burek = Dog("burek",6,"bury")
    azor = Dog("azor",3,"bialy")
    garnuch = Dog("garnuch",5,"czarny")
    burek.sound()
    azor.sound()
    garnuch.sound()
   