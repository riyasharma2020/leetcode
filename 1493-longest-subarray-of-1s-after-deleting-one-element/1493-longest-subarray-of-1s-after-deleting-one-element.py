class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k=0
        a=[]
        if 0 not in nums:
            return(len(nums)-1)
        for i in nums:
            if i==1:
                k+=1
            else:
                a.append(k)
                a.append(0)
                k=0
        if k!=0:
            a.append(k)
        print(a)
        b=[]
        for i in range(1,len(a)-1):
            b.append(a[i-1]+a[i+1])
        print(b)
        return(max(b))
            
        