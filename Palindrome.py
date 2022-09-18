a =int(input())
w=0
r1=a%10
while a>0:
    r=a%10
    a=a//10
if r-r1==0:
    print(True)
else:
    print(False)