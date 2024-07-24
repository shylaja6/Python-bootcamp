# print the unique characters in a string(not repeating)
str=input()
inp=str.lower() 
ans=""
vowel="aeiou"
consonent="bcdnghjklmnpqrstuvwxyz"
for i in inp:
    if (i not in ans):
        ans+=i
print(ans)
