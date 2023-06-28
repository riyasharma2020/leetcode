class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==-121:
            return(False)
        b=str(x)
        return(b==b[::-1])