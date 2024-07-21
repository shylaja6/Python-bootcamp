#my_list=[1,2,3,4,-4,0,-7]
#my_list.append(9999)
'''print(*my_list) #keeping * removes the square brackets
my_list.insert(0,999) #insert 999 in 0 index
print(len(my_list)) #length of list
my_list.pop() #pops the last element
my_list.pop(2) #pops the element of 2nd index
print(*my_list)
 
my_list2=[5,6,7,8]
new_list=my_list+my_list2 #concatenates 2 list
print(*new_list)


new_list=my_list.copy()
new_list.pop()
print(*new_list)'''


'''cnt=my_list.count(2)
print(cnt)

my_list.sort() #dont print anything but sorted
print(*my_list) #prints the sorted list




cnt=my_list.count(4) #counts the element 4(how many times 4 is there in list)
print(cnt)

my_list.pop(4) #pops the index 4 element
print(my_list)'''


#map means more than one elemet, input() , split("")(for space) 
# my_list=list(map(int,input().split(" "))) #dynamic taking user values(space separated)(",")
# print(*my_list)

'''list=["shylaja","chitty","shylu"]
list.append("akshi")
list.pop(2)
# cnt=list.count("akshi") #cannot count strings
print(*list)'''

#take imput from the user if user enters 1.append 2.pop 3.sort 4.print(len) declare choice as variable
#of user 

my_list=list(map(int,input().split(" ")))
print("enter 1 to append")
print("enter 2 to pop")
print("enter 3 to sort ")
print("enter 4 for len")
choice=int(input())
if(choice==1):
    my_list.append(99)
    print(my_list)
elif(choice==2):
    my_list.pop()
    print(my_list)
elif(choice==3):
    my_list.sort()
    print(my_list)
else:
    print("hello",len(my_list))
print(*my_list)
