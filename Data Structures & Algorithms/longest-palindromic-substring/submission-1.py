class Solution:
    def longestPalindrome(self, s: str) -> str:
        # create a list of strings 
        # need to somehow keep track of all the possible combos of list of strings
        # start w max then go smaller and smaller

        i = len(s)
        while i > 0:
            j = 0
            while j < len(s)-i+1:
                curr = s[j:j+i]
                #print(curr)
                #print(curr[::-1])
                if curr == curr[::-1]: 
                    return curr
                j += 1
            i -= 1