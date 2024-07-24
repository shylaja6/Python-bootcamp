# i/p=hello 123    o/p=6
s="hello 123"
sum=0
check="0123456789"
inp=s.lower()
for i in inp:
    if (i in check):
        sum+=int(i)
print(sum)



        