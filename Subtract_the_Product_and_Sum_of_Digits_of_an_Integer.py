a =int(input())
t1=0
t2=1
while a>0:
    a1=a%10
    t1+=a1
    t2*=a1
    a=a//10
print(t2-t1)