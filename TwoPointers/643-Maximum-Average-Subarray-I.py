class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i=0
        n=len(nums)
        r=0
        maxi=float('-inf')
    
        for j in range(n):
            r+=nums[j]
            l=j-i+1
            if l==k:
                avg=r/k
                maxi=max(avg,maxi)
                r-=nums[i]
                i+=1
            
        return maxi