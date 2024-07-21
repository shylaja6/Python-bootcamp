#you are given a space separated integer list .find no of even elements , no of odd elements in given list

n=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(n)):
    if(n[i]%2==0):
        even+=1
    else:
        odd+=1
print(even,odd)
#print(even)
#print(odd)