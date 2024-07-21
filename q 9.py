# 1 write a program to find area of a circle
# 2 write  a program to find perimeter of circle
# 3 write a program to find area of a triangle
# 4 write a program to find perimeter of a triangle
# finding a prime number using sqrt method


radius=4
pi=22/7
area=pi*radius*radius
print("area of circle :",area)


radius=4
pi=22/7
perimeter=2*pi*radius
print("perimw=eter of circle:",perimeter)


b=3
h=5
area=0.5*b*h
print("area of triangle:",area)


b=3
h=4
l=5
perimeter=l*h*b
print("perimeter of triangle:",perimeter)

N=[10,20,30]
a=0
for i in range(0,N[0],3):
    a+=1
for i in range(0,N[1],3):
    a+=1
for i in range(0,N[2],3):
    a+=1
print(a)
