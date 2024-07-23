# leap year or not
'''year=int(input()) 
count=0
if year%400==0: 
    count+=1
print("leap year")'''


#no of leap year in given range


for i in range(2000,2024):
    if i%400==0 or i%4==0 or i%100==0:
        print(i)    


