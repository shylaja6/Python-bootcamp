class Myclass:
    def add(a,b):
        return a+b
    def mul(a,b):
        return a*b
    def sub(a,b):
        return a-b
    def div(a,b):
        return a/b
    def rem(a,b):
        return a%b
obj1=Myclass
print(obj1.add(2,5))
print(obj1.mul(2,5))
print(obj1.rem(2,5))
print(obj1.sub(2,5))
obj2=Myclass
print(obj2.div(2,7))