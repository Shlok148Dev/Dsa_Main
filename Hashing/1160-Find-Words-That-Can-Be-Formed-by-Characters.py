from collections import defaultdict
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt=Counter(chars)
        good=0
        for i in words:
            cnt2=Counter(i)
            can_form=True
            for let in cnt2:
                if cnt2[let]>cnt[let]:
                    can_form=False
                    break
           
            if can_form:
                good+=len(i)
        return good
            
