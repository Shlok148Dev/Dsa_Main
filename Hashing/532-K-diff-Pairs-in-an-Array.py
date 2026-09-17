from collections import defaultdict

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        count = 0

        for num in nums:
            mp[num] += 1

        if k == 0:
            for num in mp:
                if mp[num] >= 2:
                    count += 1
        else:
            for num in mp:
                if num + k in mp:
                    count += 1

        return count