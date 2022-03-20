def recyclePens(n,r,k,c):
    s=1
    e=n
    while s<=e:
        m=(s+e)>>1
        amount=r+(n-m)*k
        if m*c<=amount:
            s=m+1
        else:
            e=m-1
    return e
n=int(input())
for i in range(n):
    n,r,k,c=map(int,input().split())
    print(recyclePens(n,r,k,c))
