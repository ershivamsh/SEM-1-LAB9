x=input().split()
rn=[]
r=0
tt=0
t=0
b=0
w=0
for i in x:
    if i==w:
        w+=1
        t+=1
    elif i==6 or i==4:
        b+=1
        tt+=int(i)
        t+=1
        
    else:
        t+=1
        tt+=int(i)
    
    if t==6:
        r+=tt
        rn.append(tt)
        tt=0
        t=0
print("total",r)
print("wickets",w)
print("boundries",b)
print("runs per over",rn)