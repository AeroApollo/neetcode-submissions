class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        s = s.replace(" ","").lower()
        print(s,s[::-1])
        if s == s[::-1]: return True
        return False
        '''
        '''
        new =""
        for c in s:
            if c.isalpha() or c.isdigit():
                new += c.lower()
        if new == new[::-1]: return True
        return False
        '''
        i = 0
        j = len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j-=1 
                continue
            if s[i].lower() != s[j].lower():
                return False
            i +=1 
            j -= 1
        return True
