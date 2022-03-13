def isprime(n):
    fc=0
    if n==1:
        return False
    for i in range(1,n+1):
        if(n%i==0):
            fc+=1
    if fc==2:
        return True
    else:
        return False
dic={}
a,b=map(int,input().split())
s=0
c=0
for i in range:
    if isprime(i):
        c+=1
    if c%2:
        s+=i
    else:
        s=abs(s-i)
print(s)
""""
for i in range(a,b+1):
    if isprime(i):
        if i not in dic:
              dic[i]=1
for k,v in dic.items():
    if
    """""


    

        
        
















""""
i=1
k=1
f=n
while i<=r and k<=r:
    n=n+1
    if isprime(n):
        i+=1
    f-=1
    if isprime(f):
           k+=1
if f<=1:
    print(n)
    print(-1)
else:
    print(n,f)
if 

"""""
