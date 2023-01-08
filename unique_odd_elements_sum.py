a=int(input())
l=list(map(int,input().split()))
f=list(set(l))
s=0
p=[]
for k in f:
    if k is not p and k%2==1:
        p.append(k)
for i in p:
    s+=i
print(s)