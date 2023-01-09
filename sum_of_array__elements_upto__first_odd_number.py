a=int(input())
l=list(map(int,input().split()))
s=0
c=[]
for i in l:
    if i%2==0:
        c.append(i)
    else:
        break
for k in c:
    s+=k
print(s)