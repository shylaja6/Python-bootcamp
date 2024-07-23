'''a=int(input()) 
b=int(input())
c,d=a,b
while b!=0:
    a,b=b,a%b
print((c*d)//a)'''


#prime or not
a=int(input())
r=a**0.5                   #square root of number
count=0
for i in range(2,int(r+1)):          #integer value of square+1 value
    if a%i==0:
        count=1
        break
if count==0:
    print("prime")
else:
    print("not prime")






