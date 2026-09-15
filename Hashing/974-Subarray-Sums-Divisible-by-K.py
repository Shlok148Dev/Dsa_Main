from collections import defaultdict 
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp=defaultdict(int)
        n=len(nums)
        p=[0]*n
        mp[0]=1
        count=0
        for i in range(n):
            if i==0:
                p[i]=nums[0]
            else:
                p[i]=p[i-1]+nums[i]
            r=p[i]%k
            if r in mp:
                count+=mp[r]
            mp[r]+=1
        return count
