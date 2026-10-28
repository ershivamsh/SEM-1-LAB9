x=input().split()
l=0
ll=""
for i in x:
    if len(i)>l:
        l=len(i)
        ll=i
print(ll)