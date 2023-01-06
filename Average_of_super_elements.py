a=int(input())
b=list(map(int,input().split()))
c=[]
op=0
for i in b:
    if b.count(i)==i:
        if i in c:
            continue
        c.append(i)
if len(c)>0:
    op=(sum(c)/len(c))
    op1="{:.2f}".format(op)
    print(op1)
else:
    print("-1")
    
    
    
        
        