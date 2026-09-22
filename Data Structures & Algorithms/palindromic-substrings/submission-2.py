class Solution:
    def countSubstrings(self, s: str) -> int:
        # i would do a sliding window approach
        # increasing window size and just brute force loop through
        '''
        window = 1
        total = 0 #len(s)
        while window <= len(s):
            for i in range(len(s)-window+1):
                phrase = s[i:i+window]
                if phrase == phrase[::-1]: total+=1
            window += 1
        return total
        '''
        res = 0

        for i in range(len(s)):
            # odd 
            l = r = i
            while l >= 0 and r <len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
        for i in range(len(s)):
            #even
            l = i 
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res