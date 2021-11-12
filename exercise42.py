## Animal is-a object
class Animal(object):
    
    def animalTest():
        print("Animals are living members of the animal kingdom which we are very familiar with.")

## dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        # dog has-a attribute 'name'
        self.name = name

    def dogName(self):
        print(self.name)
        print(f"Incessant barking from {self.name}")

## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        # cat has-a attribute 'name'
        self.name = name

    def catName(self):
        print(self.name)

## person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a attribute(s) name and pet
        self.name = name
        self.pet = None

    def hasPet(self):
        if self.pet != None:
            print(f"Yay, {self.name} has a pet whose name is {self.pet.name}")
        else:
            print(self.name, "is lonely and has no pet.")

## employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        # employee has-a attribute 'salary'
        self.salary = salary
    
    def wastedLife(self):
        print(f"{self.name} wastes the best years of their life only to make {self.salary} a year and in the end will just have a few bad years at the end of their life.")

## fish is-a object
class Fish(object):

    def fishFact():
        print("Fish have gills instead of lungs and live in the water. Their version of drowning is being on land. Ironic.")

# salmon is-a fish
class Salmon(Fish):

    def salmonFact():
        print("Salmon must run a gauntlet to get to their breeding grounds because bears love to eat them.")

# halibut is-a fish
class Halibut(Fish):

    def halubutFact():
        print("Halibut is flat fish that people supposedly like to eat. Idk what it tastes like.")


# rover is-a dog
rover = Dog("Rover")

# satan is-definitely-a cat
satan = Cat("Satan")

# Mary is-a person
mary = Person("Mary")

# Frank is-a(n) employee (who makes 120000)
frank = Employee("Frank", 120000)

# frank's pet is rover
frank.pet = rover

mary.pet = satan

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

# harry is-a halibut
harry = Halibut()

frank.wastedLife()
mary.hasPet()