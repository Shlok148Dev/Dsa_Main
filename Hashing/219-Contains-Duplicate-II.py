from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        mp=defaultdict(int)
        n=len(nums)
        for i in range(n):
            r=nums[i]
            if r in mp and (abs(i-mp[r])<=k):
                return True
            mp[nums[i]]=i
        return False