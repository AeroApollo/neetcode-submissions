class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        freqs = {}
        for i in nums:
            if i not in freqs:
                freqs[i] = 0
            freqs[i] += 1
        return sorted(freqs,key=lambda x:-freqs[x])[:k]
        '''
        '''
        freqs = {}
        for i in nums:
            freqs[i] = 1 + freqs.get(i,0)
        return sorted(freqs,key=lambda x:-freqs[x])[:k]
        '''
        freqs = {}
        for i in nums:
            freqs[i] = 1 + freqs.get(i,0)
        heap = []
        for num in freqs.keys(): #iterate through keys
            heapq.heappush(heap,(freqs[num],num))
            if len(heap) > k:
                heapq.heappop(heap) #pop smallest value in heap if heap exceeds k
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
            