import numpy
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        a=[]
        b=[]
        n=len(nums)
        if k==0:
            return(nums)
        a = [-1] * n
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(k,n-k):
            a[i]=((prefix[i+k+1]-prefix[i-k])//(2*k+1))
        
        
        return(a)
            
            
            
        