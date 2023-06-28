#User function Template for python3

class Solution:
    def isPallindrome(self, N):
        n=str(N)
        a=""
        while N>0:
            a+=str(N%2)
            N=int(N/2)
        #print(a)
        i=0
        if a==a[::-1]:
            i=1
        return (i)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.isPallindrome(N))
# } Driver Code Ends