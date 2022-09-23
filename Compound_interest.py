a,b,c=map(int,input().split())
t=(a*b*c)*100
t2=a*pow(1+(b/100),c)
print("%.2f"%t2)