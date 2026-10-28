x=input().split()
even=[]
odd=[]
for i in x:
    i=int(i)
    if i%2==0:
            even.append(i)
    else:
            odd.append(i)
        
print("Even numbers:",even)
print("odd numbers:",odd)