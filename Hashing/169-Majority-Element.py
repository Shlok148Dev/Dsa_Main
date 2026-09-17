from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt=Counter(nums)
        n=len(nums)
        maxi=0
        for i in cnt:
            maxi=max(maxi,cnt[i])
        for i in cnt:
            if cnt[i]>(n/2) and cnt[i]==maxi:
                return i
 