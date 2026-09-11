class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a letter tracker list for s and t 
        # if they are equal to each other return True else False
        l1, l2 = [0]*26, [0]*26
        if len(s) != len(t): return False
        i = 0 
        while i < len(s):
            l1[ord(s[i])-ord('a')]+= 1
            l2[ord(t[i])-ord('a')]+= 1
            i+=1
        if l1 == l2: return True
        return False