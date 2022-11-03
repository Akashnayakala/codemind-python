def add(a):
    r=0
    while a>0:
        c=a%10
        r+=c
        a=a//10
    return(r)
a=int(input())
while a>10:
    b=add(a)
    a=b
print(b)
    
    
        
        
    
    