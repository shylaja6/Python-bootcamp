#find the maximum element in the given list 
#test case:0   12 23 36 44 45 57       o/p 57
# test case:1   56 78 -8 12 34 -99    o/p 78

n=[12,23,36,44,45,57]

'''for i in range(0,len(n)):
    if(n[i]<n[i+1]):
        print(n[i+1])
    else:
        print(n[i])'''
max=n[0]
for i in range(len(n)):
    if(n[i]>max):
        max=n[i]
print(max)       