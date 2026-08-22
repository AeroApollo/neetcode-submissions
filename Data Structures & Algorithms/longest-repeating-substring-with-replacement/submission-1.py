class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       #similar sliding window as last problem but we need to add a tolerance of k
       # we want to keep track of the most occurring letter because we want to keep that
       # we want to change ANY other letter
       # only after number of unqiue letters > k or number of non_most occuring letters > k do we start rm letters

        # BBABXBCB or BBCCCBBB

        # how to keep track of most occur let: have counters for EACH letter => dict
        
        charSet = {}
        left = 0
        res = 0
        for right in range(len(s)):
            charSet[s[right]] = 1+charSet.get(s[right],0)

            while right-left+1 - max(charSet.values()) > k:
                charSet[s[left]] -= 1
                left +=1 
            res = max(res,right-left+1)
        return res
            
            