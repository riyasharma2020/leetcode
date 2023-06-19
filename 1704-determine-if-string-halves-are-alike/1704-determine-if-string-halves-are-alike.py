class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        n=len(s)
        l=int(n/2)
        v= ['a', 'e', 'i', 'o', 'u']
        a=[i for i in s]
        c=0
        d=0
        for i in range(l):
            if a[i] in v:
                c+=1
        for j in range(l,n):
            if a[j] in v:
                d+=1
        return(c==d)
        
        