#  given in the integer list find the avg of elements present in the even index
'''n=list(map(int,input().split(" ")))
even=0
sum=0
avg=0
for i in range(0,len(n)):
    if(i%2==0):
        sum+=n[i]
        avg=sum/len(n)
print(avg)'''


n=list(map(int,input().split(" ")))    
sum=0
count=0
for i in range(len(n)):    #avg of sum of elements in all index
    sum+=n[i]
    count+=1
print(sum/count)

