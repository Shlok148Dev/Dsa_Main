from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt=Counter(nums1)
        n=len(nums2)
        res=[]
        for i in nums2:
            if cnt[i]>0:
                res.append(i)
                cnt[i]-=1
        return res