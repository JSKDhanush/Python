#User function Template for python3

class Solution:
    def isPossible(self, x, y, a, b):
        import math
        if math.gcd(a,b)==math.gcd(x,y):
            return 1
        else:
            return 0
            
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        x,y,a,b=map(int,input().split())
        
        ob = Solution()
        print(ob.isPossible(x,y,a,b))
# } Driver Code Ends
