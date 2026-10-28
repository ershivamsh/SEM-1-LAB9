x=input().split()
t=x.count(0)
for i in x:
    if int(i)==0:
        x.remove(i)
        x.append(i)
    
print(x)