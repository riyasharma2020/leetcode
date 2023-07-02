class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        k=1
        if x<0:
            k=-1
            x*=-1
        a=0
        while x>0:
            a=a*10+(x%10)
            x=int(x/10)
        
        if a>2147483648:
            return (0)
        else:
            return(a*k)
        