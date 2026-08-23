class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # so we make sure every letter in t is in s
        # we can keep track of the count of letters in t using a list count_t = [0]*26
        # for every substring, we keep keep track of the counts in s and compare to count_t
        # the hard part is how to get the shortest substring
        # we should start with largest window and go to smallest
            # if len(s) > len(t): return False
            # from len(s) to len(t) find counts_s and if match, update the shortest string
            # issue to address is sliding window changes as window length decreases
        #let's change: smallest to largest is faster bc we can return the first one that works
            # for window options: len(t) to len(s)
                # sliding window and check count_s==count_t append only if s is in t

        '''
        if len(t) > len(s):
            return ""

        counts_t = [0]*52 #lower case is 0 to 25 and upper case is 26-51
        for c in t:
            if c.islower():
                ind = ord(c)-ord('a')
            elif c.isupper():
                ind = ord(c)-ord('A')+26
            counts_t[ind] += 1
        #print(counts_t)

        for j in range(len(t),len(s)+1):
            i = 0
            counts_s = [0]*52
            while j <= len(s):
                curr_window = s[i:j]
                #print(curr_window)
                
                
                if counts_s == counts_t:
                    return curr_window
                i += 1
                j += 1 

        return ""
        '''
        if t == "": return ""
        count_t = {}; window = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c,0)
        have, need = 0, len(count_t)
        res, resLen = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c,0)

            if c in count_t and window[c] == count_t[c]: have += 1

            while have == need:
                # update results
                if right - left +1 < resLen:
                    res = [left,right]
                    resLen = right - left + 1
                #pop from the left of our window
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left:right+1] if resLen != float('infinity') else ""