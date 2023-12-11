# Classes and Objects, Gavin Kloeckner, v0.1

class Person: # Class names should be PascalCase
    def __init__(self, age, height, hairColor, name, weight, birthday):
        # The self keyword refers to the specific object that is being delt with
        self.age = age
        self.height = height
        self.hairColor = hairColor
        self.name = name
        self.weight = weight
        self.birthday = birthday
