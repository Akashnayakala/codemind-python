a =int(input())
x=0
t1=0
while a>0:
    a1 =a%10
    if a1>t1:
        t1=a1
    else:
        t1=t1
    
    a=a//10
print(t1)