class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in nums:
            if i not in freqs:
                freqs[i] = 0
            freqs[i] += 1
        return sorted(freqs,key=lambda x:-freqs[x])[:k]
        
            