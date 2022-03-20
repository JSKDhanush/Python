def start(n,ls):
    s=0
    e=len(ls)-1
    while s<=e:
        m=(s+e)>>1
        if n<=ls[m]:
            e=m-1
        else:
            s=m+1
    return s


def end(n,ls):
    s=0
    e=len(ls)-1
    while s<=e:
        m=(s+e)>>1
        if n>=ls[m]:
            s=m+1
        else:
            e=m-1
    return e

n=int(input())
ls=list(map(int,input().split()))
a=start(n,ls)
b=end(n,ls)
ls=[]
for i in range(a,b+1):
    ls.append(i)
print(ls)
    
    
