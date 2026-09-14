from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp=defaultdict(int)
        good=False   
        n=len(nums)
        p=[0]*n
        mp[0]=-1
        j=0
        for i in range(n):
            if i==0:
                p[i]=nums[0]
            else:
                p[i]=p[i-1]+nums[i]
            rem=p[i]%k
            if rem in mp:
                j=mp[rem]
                leng=i-j
                if i-j>=2:
                    good=True
            if rem not in mp:
                mp[rem]=i    

        return good 
        