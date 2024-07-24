# remove all the brackets(braces) from the given algebraic expressions  

str="h[e]l(lo)"
#eq=""
for i in str:
    if(ord(i)==41 or ord(i)==40 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")    #eq=eq+i
#print(eq)
  

#i/p=ABC,4    O/P=EFG
str="ABC"
for i in str:
    if(ord(i)>=65 and ord(i)<=96):
        i=ord(i)+4
        print(chr(i),end="")


inp=input()
for i in inp:
    print(chr(ord(i)+4),end="")


# xyz  x=120+3=123 --->a=97   chr(123) |   y=121+3=124  chr(124)=}
inp="xyz"


