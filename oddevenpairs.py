n=int(input())
m=list(map(int,input().split()))
dic={}
for i in m:
    if i not in  dic:
        dic[i]=1
    else:
            dic[i]+=1
c=[]
d=[]
for k,v in dic.items():
    if k==v:
        c.append(k)
for i in m:
    if i in c and i not in d:
        d.append(i)
if len(d)==0:
    print(-1)
else:
    print(*d)
