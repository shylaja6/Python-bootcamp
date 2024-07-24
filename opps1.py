#single 
class Animal:
    def speak():
        return "Animal is speaking" 
    #single inheritance
class dog(Animal):
    def bark():
        return "bow..."
obj1=Animal
obj2=dog
print(obj1.speak())
print(obj2.bark())
#multi level inheritance
class puppy(dog):
    def puppy_speak():
        return "im puppy"
obj3=puppy
print(obj3.puppy_speak())

