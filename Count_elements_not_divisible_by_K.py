a,b=map(int,input().split())
l=list(map(int,input().split()))
c=[]
d=0
for i in l:
    if i%b!=0:
        d+=1
        c.append(i)
print(d)
        