x=input().split()
min=12345678
max=-987654
for i in x:
    i=int(i)
    if i >max:
        max=i
    if i<min:
        min=i
print("min",min)
print("max",max)