class Solution:
    def longestPrefix(self, s: str) -> str:
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
        return(s[0:k])
        