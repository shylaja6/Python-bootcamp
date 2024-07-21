# replace the elements in the array with average of maximum and minimum element
# 1: 13 2 67 20 68
# 68+2=70/2=35
# 35 35 35 35 35

n=[13,2,67,20,68]
'''max=n[0] 
min=n[0]
for i in range(len(n)):
    if(n[i]>max):
        max=n[i]
    else:
        min=n[i]
sum=max+min
average=sum/2
print(average)'''



max=n[0]
for i in range(len(n)):
    if(n[i]>max):
        max=n[i]
#print(max)
min=n[0]
for i in range(len(n)):
    if(n[i]<min):
        min=n[i]
#print(min)
avg=(max+min)/2
#print(avg)
for i in range(len(n)):
    n[i]=avg
print(n)