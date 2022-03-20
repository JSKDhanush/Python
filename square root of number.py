def floorSqrt(x):
        e=x
        s=1
        m=x//2
        while s<=e:
            if m*m==x:
                return m
            elif m*m>x:
                e=m-1
                m=(s+e)>>1
            elif m*m<x:
                s=m+1
                m=(s+e)>>1
        return m
x=int(input())
print(floorSqrt(x))
           
                 
            
  
