from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt=Counter(magazine)
        cnt2=Counter(ransomNote)
        for i in ransomNote:
            if cnt2[i]>cnt[i]:
                return False
        return True