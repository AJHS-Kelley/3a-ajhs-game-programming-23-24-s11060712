# Classes and Objects, Gavin Kloeckner, v0.3.1

class Person: # Class names should be PascalCase
    def __init__(self, age, height, hairColor, name, weight, birthday):
        # The self keyword refers to the specific object that is being delt with
        self.age = age
        self.height = height
        self.hairColor = hairColor
        self.name = name
        self.weight = weight
        self.birthday = birthday

    #__str__ Method Format
    def __str__(self):
        return f"{self.name} is {self.age} years old.\nThey are {self.height} and their birthday is {self.birthday}.\nThey weigh {self.weight} lbs and have {self.hairColor} color hair.\n"



# A class is a 'blueprint' to make an object

examplePerson = Person(17, '5\'9\"', 'brown', 'Gavin', 122, 'July 17')
examplePerson2 = Person(31, '6\'1\"', 'black', 'John', 200, 'April 31')
print(examplePerson)

# Changing Properties After Creating Object
print(examplePerson2.age)
examplePerson2.age = 320
print(examplePerson2.age)
print(examplePerson2.birthday)
examplePerson2.birthday = "March 05"
print(examplePerson2.birthday)
