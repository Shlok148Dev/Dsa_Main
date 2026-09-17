from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cnt=Counter(nums)
        sol=[]
        n=len(nums)
        for i in cnt:
            if cnt[i]>n/3:
                sol.append(i)
        return sol