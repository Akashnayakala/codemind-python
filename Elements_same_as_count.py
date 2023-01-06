a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if b.count(i)==i:
        if i in c:
            continue
        c.append(i)
if len(c)==0:
    print("-1")
else:
    print(*c)