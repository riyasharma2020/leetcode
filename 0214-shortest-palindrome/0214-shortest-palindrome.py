class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # i=0
        # j=len(s)-1
        # k=1
        # while(k):
        #     s1=s[i:j+1]
        #     if s1==s1[::-1]:
        #         k=0
        #     else:
        #         j-=1
        # b=s[j+1:]
        # b=b[::-1]+s
        # return(b) this logic ran in O(n square), so we optimised approach to make time complexity O(n)
        t=s
        # s="aaabaaaaab"
        s=s+"#"+s[::-1]
        a=[i for i in s]
        lps=[]
        i=1
        le=0
        lps.append(0)
        l=len(a)
        while(i<l):
            if a[i]==a[le]:
                le+=1
                lps.append(le)
                i+=1
            else:
                if le!=0:
                    le=lps[le-1]
                else:
                    lps.append(0)
                    i+=1
        k=lps[-1]
        b=t[k:]
        t=b[::-1]+t
        return(t)