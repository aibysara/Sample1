#Polymorphism means one thing having many forms
class Animal:
    def sound(self):
        print("Animal creates sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")
class Cat(Animal):
    def sound(self):
        super().sound()
        print("Meow")

d=Dog()
d.sound()
c=Cat()
c.sound()

