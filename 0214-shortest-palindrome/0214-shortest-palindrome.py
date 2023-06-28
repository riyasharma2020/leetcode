class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i=0
        j=len(s)-1
        k=1
        while(k):
            s1=s[i:j+1]
            if s1==s1[::-1]:
                k=0
            else:
                j-=1
        b=s[j+1:]
        b=b[::-1]+s
        return(b)