from collections import defaultdict
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        p=[0]*n
        lsum=0
        total=sum(nums)
        for i in range(n):
            if i==0:
                p[i]=nums[0]
            else:
                p[i]=p[i-1]+nums[i]
            if i!=0: lsum=p[i-1]
            if i==0: lsum=0
            rsum=total-p[i]
            if lsum==rsum:
                return i
        return -1