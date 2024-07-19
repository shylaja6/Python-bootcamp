mr_x="badminton"
mr_y="tabletennis"
mr_z="swimming"
selected=mr_z
heightx=int(input("enter height of x:"))
weightx=int(input("enter weight of x:"))
bodyx=int(input("enter bodyfat:"))
zmedals=(50/100)*14
heighty=int(input("enter height of y:"))
weighty=int(input("enter weight of y:"))
bodyy=int(input("enter bodyfat:"))
if(heightx>=140) and (weightx<=148) and (bodyx<12):
    if(heighty>=118 or heighty<=148) and weighty%zmedals==0 and bodyy==14:
        print("all went in same plane")
    else:
        print("only x,z went in same plane")
else:
    print("only z went in plane")