from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mp=defaultdict(int)
        n=len(nums)
        count=0
        for i in range(n):
            r=k+nums[i]
            t=nums[i]-k
            if (r in mp) or (t in mp):
                count=count+mp[r]+mp[t]
            mp[nums[i]]+=1
        return count