a =int(input())
r=0
for i in range(1,a,1):
    if a%i==0:
        r+=i
if r>a:
    print("True")
else:
    print("False")
