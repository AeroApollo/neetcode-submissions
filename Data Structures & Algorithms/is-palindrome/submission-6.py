class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0; j = len(s)-1
        #print(i,j,s[i],s[j])
        while i < j:
            #print(i,j,s[i],s[j])
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i+=1
                j-=1
            '''
            if (s[i].isalpha() and s[j].isdigit()) or (s[i].isdigit() and s[j].isalpha()):
                return False
            elif s[i].isalpha() and s[j].isalpha() and s[i].lower() != s[j].lower(): 
                return False
            elif s[i].isdigit() and s[j].isdigit() and s[i] != s[j]:
                return False
            else:
                i+=1
                j-=1
            '''
        return True
            
            
