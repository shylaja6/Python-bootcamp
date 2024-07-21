#find the sum of sqauares of given numbers
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r*r   #r**2
    n=n//10
print(sum)