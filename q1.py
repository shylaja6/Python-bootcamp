# mr x is trying to create a new password for his instagram account.these are the required conditions for creating a new password
# condition1.minimum length is 8 and max length is 15
# 2.only @,/ is allowed in a password
# 3.no spaces are allowed
# 4.only alpha numerics are allowed
# you are supposed to print weak if length is exact 8
# medium-length b/w 8 to 12
# strong if len is b/w 12 to 15


password=input()
l=len(password)
count=0
if l>=8 and l<=15:
    for i in password: 
        # if i==" ":  
            # print("invalid")
            # break
        if i=="@" or i=="/":
            count+=1 
        if i==" ":  
            print("invalid")
            break    
if l==8:
    print("pass is weak")
if l>8 and l<12:
    print("pass is medium")
if l>12 and l<=15:
    print("pass is strong")       
