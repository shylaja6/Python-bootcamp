# how to reverse a number
# 123
# 321

n=123
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(int(rev))