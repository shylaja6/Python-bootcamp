n=int(input())
if(n%2==0 and n>=1):
    print("even and positive")
elif(n%2==0 and n<1):
    print("even and negative")
elif(n%2!=0 and n>=1):
    print("odd and positive")
else:
    print("odd and negative")