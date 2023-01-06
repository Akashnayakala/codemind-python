a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if b.count(i)==i:
        if i in c:
            continue
        c.append(i)
print(len(c))