from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split()
        mp=defaultdict(int)
        mp2=defaultdict(int)
        for i in range(len(pattern)):
            if len(pattern)!=len(word):
                return False
            if pattern[i] in mp  and mp[pattern[i]]!=word[i]:
                return False
            mp[pattern[i]]=word[i]
            if word[i] in mp2 and mp2[word[i]]!=pattern[i]:
                return False
            mp2[word[i]]=pattern[i]
        return True