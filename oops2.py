#inheritance and multiple


class father:
    def father_speak():
        return "father class"
class mother:
     def mother_speak():
            return "mother class"
class kid(father,mother):
    def kid_speak():
     return "im a kid . im having properties"
obj1=kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())