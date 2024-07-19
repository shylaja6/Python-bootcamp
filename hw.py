import math
n=int(input())
sq=int(math.sqrt(n))
i=2
while i<=sq:
    if sq%i==0:
        break
    i=i+1
if i==sq:
    print("prime")
else:
    print("not prime")
