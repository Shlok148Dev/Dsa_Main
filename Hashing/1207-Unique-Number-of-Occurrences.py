from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = defaultdict(int)

        for num in arr:
            mp[num] += 1

        freq = defaultdict(int)

        for num in mp:
            freq[mp[num]] += 1

        for num in freq:
            if freq[num] > 1:
                return False

        return True