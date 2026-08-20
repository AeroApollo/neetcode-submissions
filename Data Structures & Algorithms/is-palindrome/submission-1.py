class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        s = s.replace(" ","").lower()
        print(s,s[::-1])
        if s == s[::-1]: return True
        return False
        '''
        new =""
        for c in s:
            if c.isalpha() or c.isdigit():
                new += c.lower()
        if new == new[::-1]: return True
        return False
