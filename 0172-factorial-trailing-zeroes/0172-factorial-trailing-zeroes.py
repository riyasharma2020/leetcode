class Solution:
    def trailingZeroes(self, n: int) -> int:
        b=0
        while(n>4):
            d=n%5
            n=n-d
            n=n//5
            b+=n
        return(b)