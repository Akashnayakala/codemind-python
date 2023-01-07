a=int(input())
l=list(map(int,input().split()))
l2=[]
d=0
for i in l:
    if i not in l2:
        l2.append(i)
for j in l2:
    d+=j
print(d)
    
    