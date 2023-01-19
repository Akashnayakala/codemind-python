a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
l4=[]
count=0
for i in l1:
    if i not in l3:
        l3.append(i)
for k in l2:
    if k not in l4:
        l4.append(k)
for m in l3:
    if m not in l4:
        count+=1
for n in l4:
    if n not in l3:
        count+=1
print(count)
