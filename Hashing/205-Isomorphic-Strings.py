from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp=defaultdict(int)
        mp2=defaultdict(int)
        for i in range(len(s)):
            if len(s)!=len(t):
                return False
            if s[i] in mp  and mp[s[i]]!=t[i]:
                return False
            mp[s[i]]=t[i]
            if t[i] in mp2 and mp2[t[i]]!=s[i]:
                return False
            mp2[t[i]]=s[i]
        return True