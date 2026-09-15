from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        mp=defaultdict(int)
        good=0
        n=len(nums)
        total=(n*(n-1))//2
        for i in range(n):
            eq=i-nums[i]
            if eq in mp:
                good+=mp[eq]
            mp[eq]+=1
        bad=total-good
        return bad
