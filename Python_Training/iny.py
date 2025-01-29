class Animal:
    def __init__(self,name):
        self.name = name
        self.species = "Animal"
        self.is_alive = True

    def make_sound(self, sound=None):
        if sound is None:
            return "This animal makes no sound"
        else:
            return f"This animal says {sound}"
        
    def eat(self,food):    
        print(f"{self.name} is eating {food}")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def spqeak(self):
        return "WOOF!"

class Snail(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.is_alive = False

    def make_sound(self):
        return super().make_sound(None)

class Cat(Animal):
    def make_sound(self, sound=None):
        if sound is None:
            return "MEOW!"
        else:
            return f"This animal says {sound}"

dog = Dog("Duffy")

cat = Cat("Flerken")

snail = Snail("Neil")
print(cat.make_sound())
print(dog.name)
print(snail.make_sound())
print(cat.speak())
print(snail.is_alive)