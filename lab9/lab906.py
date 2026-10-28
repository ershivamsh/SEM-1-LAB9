m=input().split()
r=input().split()
kh=input().split()
p=len(m)
tt=0
t={}
for i in range(p):
    t[m[i]]=r[i]
for k in kh:
    tt+=int(t[k])
    print(k,t[k])
print("total",tt)