class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        sublists = []
        anagrams = {}
        for word in strs:
            base_letters = str(sorted(word))
            if base_letters not in anagrams:
                anagrams[base_letters] = [word]
            else:
                anagrams[base_letters].append(word)
        #print(anagrams)
        for ana, ana_list in anagrams.items():
            #print(ana)
            sublists.append(ana_list)
        return sublists
        '''
        anagrams = {}
        for word in strs:
            counts = [0]* 26 # create a counter for each of 26 letters
            for c in word:
                counts[ord(c)-ord('a')] += 1
            key = tuple(counts)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())