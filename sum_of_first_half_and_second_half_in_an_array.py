a=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
c=[]
d=[]
x1=len(l)/2
x2=len(l)//2
x3=0
if x1==x2:
    x3=x2
else:
    x3=x2
for i in l[:x3]:
    s1+=i
for k in l[x3:]:
    s2+=k
print(abs(s1))
print(s2)