a=int(input())
b=list(map(int,input().split()))
n=int(input())
c=[]
for i in b:
    if b.count(i)==n:
        if i in c:
            continue
        c.append(i)
if len(c)==0:
    print("-1")
else:
    print(*c)