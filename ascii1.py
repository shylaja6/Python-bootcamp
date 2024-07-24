print(ord('A'))
print(chr(65))
for i in range(0,128):
    print(chr(i),end=" ")

for i in range(32,128):    #special characters
    print(chr(i),end=" ")

#sum of digits in a number using ascii value

str="hello 1234world"
sum=0
for i in str:
    if (ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)




# write a code to print all the capital letters in a given string
str="HELlo"
for i in str:
    if(ord(i)>=65 and ord(i)<=96):     #97 to 122 for lower casee
        print(i,end=" ")

    
