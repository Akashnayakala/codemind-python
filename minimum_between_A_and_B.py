a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
c2=[]
c1=0
m1=max(b,c)
m2=min(b,c)
for i in l:
    if i>=m2 and i<=m1:
        c2.append(i)
        c1=1
if c1==0:
    print("-1")
else:
    print(min(c2))


    