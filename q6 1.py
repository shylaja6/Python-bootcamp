#you are given a , separated natural numbers 1 to 10
#print only the even numbers

#n=[1,2,3,4,5,6,7,8,9,10]           #direct input
n=list(map(int,input().split(",")))  #if we take user input 
#for i in range(len(n)):
 #   if(i%2==0):
  # 
  
count=0
for i in range(1,len(n),2):
 #   print(n[i])
 count+=1
print(count)