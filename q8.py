# i/p=hello---wor---ld    o/p=------helloworld     "-",30


input="----hello--wor--ld"
count=0
ans=""
for i in input:
    if(i=='-'):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)



newstr=input.replace('-','')
str=input.count('-')
result='-'*str+newstr
print(result)