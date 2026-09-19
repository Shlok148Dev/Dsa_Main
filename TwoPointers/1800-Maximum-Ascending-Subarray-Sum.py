class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        
        maxi=0
        n=len(nums)
        r=nums[0]
        for j in range(n):
            if nums[j]>nums[j-1] and j!=0:
                r+=nums[j]
            else:
                r=nums[j]
               
            maxi=max(r,maxi)
        return maxi