#method over loading

class cal:
    def add(self,*args):
        return sum(args)
obj1=cal
print(obj1.add(1,2))
print(obj1.add(1,2,3))