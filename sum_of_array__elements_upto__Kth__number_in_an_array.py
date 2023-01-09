a=int(input())
l=list(map(int,input().split()))
b=int(input())
s=0
c=[i for i in l if i<=b]
for k in c:
    s+=k
print(s)