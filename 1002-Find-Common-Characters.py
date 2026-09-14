from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt=Counter(words[0])
        n=len(words)
        res=[]
        for i in range(1,n):
            cnt2=Counter(words[i])
            for ch in cnt:
                cnt[ch]=min(cnt[ch],cnt2[ch])
        for ch in cnt:
            while cnt[ch]>0:
                res.append(ch)
                cnt[ch]-=1
        return res