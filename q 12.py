#minimum element

n=[12,23,36,44,45,57]
min=n[0]
for i in range(len(n)):
    if(n[i]<min):
        min=n[i]
print(min)