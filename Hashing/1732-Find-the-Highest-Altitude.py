from collections import defaultdict
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        mp=defaultdict(int)
        n=len(gain)
        maxi=0
        p=[0]*(n+1)
        p[0]=0
        for i in range(1,n+1):

            p[i]=p[i-1]+gain[i-1]
            maxi=max(p[i],maxi)
        return maxi