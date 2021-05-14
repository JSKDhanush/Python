num=int(input())
min=num%10
max=num%10
c1=c2=0
temp=num
while num:
    r=num%10
    num=num//10
    if r>max:
        max=r
    elif r<min:
        min=r
num=temp
while num:
    r=num%10
    num=num//10
    if r==max:
        c1+=1
    elif r==min:
        c2+=1
print(c2,c1)
