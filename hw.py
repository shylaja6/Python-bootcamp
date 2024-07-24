# print upper triangular matrix
# print lower triangular matrix
# print rhombus
# *** 
#   ***     parallelogram 
#     ***
# number pyramid


n=int(input())
for i in range(n):
    for j in range(n):
        if(i>j):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()



n=int(input())
for i in range(n):
    for j in range(n):
        if(i<j):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()



rows = 7
for i in range (1,rows + 1):              
    for j in range (1,rows - i + 1):
        print (end=" ")
    for j in range (1,rows + 1):
        print ("*",end=" ")
    print()



rows = 7
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print()



rows = 3
cols = 4
for i in range(0, rows):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(1, cols):
        print("*", end="")
    print()


rows= 7       
for i in range(0, rows):       
        for j in range(0, i + 1):       
            print("* ", end="")       
        print()


rows = 7
for i in range (1,rows + 1):
    for j in range (1,rows - i + 1):
        print (end=" ")
    for j in range (1,rows + 1):
        print ("*",end=" ")
    print()