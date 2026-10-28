x=input()
l=[]
ss=0
for i in x:
    if i.isdigit():
        ss+=int(i)
        l.append(int(i))
print(l)
print("sum:",ss)