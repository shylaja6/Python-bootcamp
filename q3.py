# print all the vowels followed by consonants

str=input()
inp=str.lower() 
# ans=""
vowel="aeiou"
consonent="bcdnghjklmnpqrstuvwxyz"
for i in inp:
    if(i in vowel):
        print(i,end="")         #ans+=i
for i in inp:
    if(i in consonent):
        print(i,end="")