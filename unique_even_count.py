a=int(input())
l=list(map(int,input().split()))
f=list(set(l))
count=0
s=0
p=[]
for k in f:
    if k is not p and k%2==0:
        p.append(k)
        count+=1
print(count)