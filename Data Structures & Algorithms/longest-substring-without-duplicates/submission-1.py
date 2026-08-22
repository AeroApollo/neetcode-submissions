class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        #traverse the list in a for loop for c in s:
        # given an empty list sub = [] and longest = 0
        # if c is not in s: sub.append(c) 
        # else: if len(sub) > longest: longest = len(sub) and sub =[c]

        #time O(N) and space is O(number of characters in list)

        #current method doesn't take into account substring that start with a later unique char

        # if we encounter a duplicate char:
        # 1) we check if the current sub is the longest and update if needed
        # 2) remove all chars in sub up to the first instance of duplicate

        
        sub = []; longest = 0
        for c in s:
            if c not in sub: sub.append(c)
            else: #c is a duplicate
                #print(sub)
                if len(sub) > longest: #check if current sub is longest 
                    longest = len(sub)

                first_ind = sub.index(c) # index of first instance of duplicate
                sub = sub[first_ind+1:]
                sub.append(c)
                #print(sub)
                

        # last sub build was uncheck so check
        if len(sub) > longest:
            return len(sub)
        return longest
        
        # we need to keep track of multiple lists
        # each list is started by a unique letter
        # i would use a dictionary here: key = unique letter encountered, value = [c]
        # as we traverse substring ...actl we might not need a dict