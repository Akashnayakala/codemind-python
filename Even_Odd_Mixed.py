a =int(input())
even=0
odd=0
mixer=0
while a>0:
    a1=a%10
    if a1%2==0:
        even+=1
    elif a1%2!=0:
        odd+=1
    else:
        mixer+=1
    a=a//10
if even>1 and odd==0 and mixer==0:
    print("Even")
elif even==0 and odd>1 and mixer==0: 
    print("Odd")
else:
    print("Mixed")
    