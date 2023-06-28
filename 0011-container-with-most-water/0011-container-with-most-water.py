class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        n=len(height)
        r=n-1
        area=0
        while l<r:
            x=height[l]
            y=height[r]
            area=max(area,(r-l)*min(x,y))
            if x<y:
                l+=1
            else:
                r-=1
        return(area)
                
        