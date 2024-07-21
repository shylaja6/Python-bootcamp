#find the missing number in array
m=list(map(int,input().split()))
n=len(m)+1
total_sum=n*(n+1)//2
actual_sum=sum(m)  
missing=total_sum-actual_sum
print(missing)
    

