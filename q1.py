# check how many vowels are given in a string
str=input()
check=['a','e','i','o','u']
count=0
for i in str:
    if(i in check):
        count+=1
print(count)