def gcd(n,arr):
        import math
        r=arr[0]
        i=0
        while i!=len(arr)-1:
            r=math.gcd(r,arr[i+1])
            i+=1
        return r
n=int(input())
arr=list(map(int,input().split()))
print(gcd(n,arr))

      
"""
n=3
arr=2,4,6 op=2 gcd of (2,4,6)
"""
