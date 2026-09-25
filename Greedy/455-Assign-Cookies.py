class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort()
        g.sort()
        l=0
        r=0
        
        while(l<len(s) and r<len(g)):
            if s[l]>=g[r]:
                r+=1
            l+=1
        return r