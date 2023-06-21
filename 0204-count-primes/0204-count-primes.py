class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        if(n==0 or n==1or n==2):
            return(0)
        n-=1
        a=[1]*(n+1)
        for i in range(2,int(math.sqrt(n))+1):
            if a[i]==1:
                for j in range(i*i,n+1,i):
                    a[j]=0
                    # if j%i==0:
                    #     a[j]=0
        
        return(a.count(1)-2) 