a,b=map(int,input().split())
if b==a+1 or b==a-1:
    print("Yes")
elif a+b==11:
    print("Yes")
else:
    print("No")