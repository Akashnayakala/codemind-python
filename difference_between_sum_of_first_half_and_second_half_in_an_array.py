a=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
c=[]
d=[]
if a%2==1:
    l.append(l[a-1]+1)
r=len(l)//2
for i in l[:r]:
    s1+=i
for k in l[r:]:
    s2+=k
print(abs(s1-s2))
