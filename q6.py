#take a space separated input from a user and print alternate elements

# n=int(input())
# for i in range(1,n+1,2):
#     print(i)   

my_list=list(map(int,input().split()))  #alternate values of list
for i in range(0,len(my_list),2):
    print(my_list[i])