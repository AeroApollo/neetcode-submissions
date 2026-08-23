class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #since it's a permu, i thinnking sets
        # traverse s2 for a fixed window len(s1)
        # if set(window) == set(s1): return True
            # caveat for this is sets are unsorted 
                # using sorted makes at worst O(N^2) 
        
        #what is we try to track the counts of each letter
        # counts = {} => count[c 9of s1] = 1...
        # for loop to record through
        # len(s1) = fixed window for s2 where i =0 j = len(s1)-1

        #how to match s2 window counts to s1?

        # terminating condition: counts[letter] < 0
        # copy counts every while pass


        i = 0; j = len(s1)-1
        sort_s1 = sorted(s1)
        while j < len(s2):
            #print(sorted(s2[i:j+1]))
            if sort_s1 == sorted(s2[i:j+1]):
                return True
            i+=1
            j+=1
        return False