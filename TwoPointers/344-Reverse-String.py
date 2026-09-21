class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        l=0
        c=0
        r=n-1
        while(l<=r):
            c=s[l]
            s[l]=s[r]
            s[r]=c
            l+=1
            r-=1
        return s