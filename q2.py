# write a program to print all the consonants and vowels


'''str=input()
inp=str.lower()
check=['a','e','i','o','u']
count=0
count_c=0
for i in inp:
    if(i in check):
        count+=1
    else:                   
        count_c+=1

print("no of vowels",count)
print("no of consonants",count_c)'''


str=input()
inp=str.lower()
vowel="aeiou"
v=0
c=0
consonent="bcdnghjklmnpqrstuvwxyz"
for i in inp:
    if(i in vowel):
        v+=1
for i in inp:
    if(i in consonent):
        c+=1
print("no of vowels",v)
print("no of consonent",c)



    

