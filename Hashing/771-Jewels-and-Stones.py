from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt=Counter(stones)
        cnt2=Counter(jewels)
        n=len(stones)
        count=0
        for i in cnt:
            if i in cnt2:
                count+=cnt[i]
                
        return count