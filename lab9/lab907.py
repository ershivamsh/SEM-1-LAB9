x=input().split()
t=""
tt=[]
for i in x:
    for j in i:
        t=j+t
    tt.append(t)
    t = ''
print(' '.join(tt))