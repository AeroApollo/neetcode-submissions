class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t): return True
        return False
        #if sorted(set(s)) == sorted(set(t)) and len(s) == len(t): return True
