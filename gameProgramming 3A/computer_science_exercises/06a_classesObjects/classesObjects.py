# Classes and Objects, Gavin Kloeckner, v0.2

class Person: # Class names should be PascalCase
    def __init__(self, age, height, hairColor, name, weight, birthday):
        # The self keyword refers to the specific object that is being delt with
        self.age = age
        self.height = height
        self.hairColor = hairColor
        self.name = name
        self.weight = weight
        self.birthday = birthday


# A class is a 'blueprint' to make an object

examplePerson = Person(17, '5\'9\"', 'brown', 'Gavin', 122, 'July 17')
examplePerson2 = Person(31, '6\'1\"', 'black', 'John', 200, 'April 31')
print(examplePerson.age)
print(examplePerson.height)
print(examplePerson.name)

print(examplePerson2.age)
print(examplePerson2.height)
print(examplePerson2.name)
