
# patterns

'''row=5
column=5
for i in range(row): 
    for j in range(column):
        print("*",end="")
    print()'''


row=10
column=10
for i in range(row): 
    for j in range(column):
        if(i==j):
           print(" ",end="")
        else:
           print("*",end="")
    print()