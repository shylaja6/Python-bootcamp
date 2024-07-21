#find sum of all the nos using for loop
#print nos 1 to 100 using for loop
#append 1 to 100 in empty list


for i in range(1,101):
    print(i)


n=100
for i in range(1,n+1):     
     print(i,end="")

 list=[]
 for i in range(1,101):   #append 1 to 100 in empty list
     list.append(i)
 print(list)

 sum=0
 for i in range(1,101):  #sum of 1 to 100 
   sum+=i
 print(sum)


