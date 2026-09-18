from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        mp=defaultdict(int)
        n=len(nums)
        count=0
        for i in range(n):
            r=nums[i]
            if r in mp:
                count+=mp[r]
            mp[nums[i]]+=1
        return count