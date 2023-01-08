a=int(input())
l=list(map(int,input().split()))
o=[]
h1=[]
h=[i for i in l if i%2==0]
g=[i for i in l if i%2==1]
m1=min(len(h),len(g))
m2=max(len(h),len(g))
for k in range(m1):
    o.append(h[k])
    o.append(g[k])
if m2==len(h):
    h1=o+h[m1:]
if m2==len(g):
    h1=o+g[m1:]
if a%2==0:
    print(*h1)
else:
    h1.append(0)
    print(*h1)
