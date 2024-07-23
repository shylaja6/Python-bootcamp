# GCD of 2 numbers

a=int(input())               #a,b=b,a%b  a=21 b=14 now a=14 b=7 the a=7 b=0   print a value
b=int(input())
while b!=0:
    a,b=b,a%b        #assignment operator
print("GCD of a and b is",a)