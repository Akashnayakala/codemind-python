a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if i%2!=0:
        if i in c:
            continue
        c.append(i)
print(len(c))
