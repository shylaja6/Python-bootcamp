#find the  element that is  present in k+N index
#k=3
#N=2
# i/p 3 6 8 4 61 2   
#o/p is 2
# -----------
# k=3
# N=4
# 80 70 54 36 72

'''n=[3,6,8,4,61,2]
k=3
N=2
for i in range(0,len(n)):
     if(i==k+N):
          print(n[i])'''


n=[80,70,54,36,72]
k=3
N=4    
for i in range(0,len(n)):
    if(i>(N+k)):
        print("error")
print("error")