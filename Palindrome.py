a=int(input())
g=a
rev=0
t=a
d=1
while a>0:
    d=a%10
    rev=rev*10+d
    a=a//10
if rev==g:
    print("True")
else:
    print("False")
    