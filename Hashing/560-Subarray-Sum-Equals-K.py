from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mp=defaultdict(int)
        count=0
        p=[0]*n
        mp[0]=1
        for i in range(n):
            if i==0:
                p[i]=nums[0]
            else:
                p[i]=p[i-1]+nums[i]
            r=p[i]-k
            if r in mp:
                count+=mp[r]
            mp[p[i]]+=1
        return count