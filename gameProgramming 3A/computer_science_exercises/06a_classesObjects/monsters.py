# Monsters, Gavin Kleockner, v0.1

class Entity:
    def __init__(self, name, topSpeed, height, weight, dangerLvl):
        self.name = name
        self.topSpeed = topSpeed
        self.height = height
        self.weight = weight
        self.dangerLvl = dangerLvl
        
        def __str__(self):
            return f'Name of Entity: {self.name}\nSpeed of Entity: {self.topSpeed}mph\nHeight: {self.height} feet\nWeight: {self.weight}lbs\nDanger Level: {self.dangerLvl}\n'
        
    def mainPriority(self):
        print('This program will notify you if the creatur displayed is to be taken care of immedietly or not.\n')
        if self.dangerLvl > 'Class 4':
            print('Not as dangerous. Prioritize Class 4 and 5 level entities.\n')
        else:
            print('Danger level above Class4.\nRedirecting units for immediate execution of entity.\n')
        
creature = Entity('Bautre', 30, 5.6, 187, 'Class 3')
print(creature)

