# peak element
'''a=list(map(int,input().split()))
count=0
for i in range(1,len(a)-1):
    if(a[i-1]<a[i] and a[i]>a[i+1]):
        count=i 
        break
print(a[count]) '''

a=list(map(int,input().split()))
for i in range(1,len(a)-1):               #more than one peak element also there
    if a[i-1]<a[i] and a[i]>a[i+1]:
        print(a[i])    #print(a[i],end=" ")