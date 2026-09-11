class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagram is always a list that tracks letter counr [0]*26
        # the fastest to solve but brute way to solve this is a dictionary
        # key = listtrack values = list of words
        # for loop through dictionary to process for output
        anas = {}
        for word in strs:
            l_track = [0]*26
            for let in word:
                l_track[ord(let)-ord('a')] += 1
            l_track = str(l_track)
            if l_track not in anas:
                anas[l_track] = [word]
            else: 
                anas[l_track].append(word)
        #print(anas)
        output = list(anas.values())
        '''
        output = []
        for ana, ana_list in anas.items():
            output.append(ana_list)
        '''
        return output