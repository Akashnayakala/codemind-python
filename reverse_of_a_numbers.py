a=int(input())
a1=0
a2=a
d=1
while a>0:
    d=a%10
    a1=a1*10+d
    a=a//10
print(a1)
    