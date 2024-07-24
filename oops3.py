#method overwriting

class Animal:
    def speak():
        return "animal is speaking"
class dog(Animal):
    def speak():
        return "bow.."
class puppy(dog):
    def speak():
        return "puppy is speaking"
obj3=puppy
print(obj3.speak())