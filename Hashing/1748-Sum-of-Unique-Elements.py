from collections import Counter
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        n=len(nums)
        cnt=Counter(nums)
        sumy=0
        for i in cnt:
            if cnt[i]==1:
                sumy+=i       
        return sumy    