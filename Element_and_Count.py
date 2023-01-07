a=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in l:
    if i not in l1:
        l1.append(i)
for j in l1:
    l2.append(l.count(j))
for k in range(len(l1)):
    l3.append(l1[k])
    l3.append(l2[k])
print(*l3)
    


