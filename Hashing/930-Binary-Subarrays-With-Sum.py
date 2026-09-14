from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mp=defaultdict(int)
        n=len(nums)
        p=[0]*n
        mp[0]=1
        count=0
        for i in range(n):
            if i==0:
                p[0]=nums[0]
            else:
                p[i]=p[i-1]+nums[i]
            r=p[i]-goal
            if r in mp:
                count+=mp[r]
            mp[p[i]]+=1
        return count