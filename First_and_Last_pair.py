a=int(input())
p=a
l=list(map(int,input().split()))
m=l[::-1]
c=[]
for i in range(a):
    if a%2==0:
        if len(c)<a:
            c.append(l[i])
            c.append(m[i])
    else:
        if len(c)<a:
            c.append(l[i])
            if len(c)<a:
               c.append(m[i])
if p%2!=0:
    c.append(0)
    print(*c)
else:
    print(*c)