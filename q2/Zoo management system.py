# Parent class
class Animal:
    def __init__(self, name):  #attribute "name" is in the class Animal
        self.__name = name

    @property #gets the attribute name
    def name(self): #makes the private attribute accessible for inheritence
        return self.__name

    def eat(self):
        print(self.name,"is eating.")
        
    def sleep(self):
        print(self.name, "is sleeping.")

    def make_sound(self):
        print(self.name, "makes a sound")
        
# Child classes override the inherited method make_sound(), sleep(), and eat() 
class Lion(Animal):
    def make_sound(self):
        print(self.name, "roars loudly!")

    def eat(self):
        print(self.name,"eats fresh meat.")
        
    def sleep(self):
        print(self.name, "is sleeping on the soft grass.") 

#creates another child class Elephant       
class Elephant(Animal):
    def make_sound(self):
        print(self.name, "says thrumpets!")

    def eat(self):
        print(self.name,"eats grass and fruits.")
        
    def sleep(self):
        print(self.name, "is sleeping on the warm nest.")
        
#creates another child class Monkey 
class Monkey(Animal):
    def make_sound(self):
        print(self.name, "chatters!")

    def eat(self):
        print(self.name,"eats bananas.")
        
    def sleep(self):
        print(self.name, "is sleeping in the high trees.")
        
# Create objects
lion1 = Lion("Simba")
elephant1 = Elephant("Dumbo")
monkey1 = Monkey("George")

# Output the animal make_sound
animals = [lion1, elephant1, monkey1] #child classes listed 
for animal in animals: #calls them in a loop for effiency instead of individually
    animal.make_sound()
    animal.eat()
    animal.sleep()
    print("----------")
