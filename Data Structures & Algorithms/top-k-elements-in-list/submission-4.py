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
            res.append(heapq.heappop(heap)[1]) #when popping smallest value but within k, get only the key.numerical value not the count of the value
        return res
        '''
        count = {} # dict to track freqs
        freq = [[] for i in range(len(nums)+1)] #list contain sublists for the all possible freqs (which is up to the length of nums)
        for num in nums:
            count[num] = 1 + count.get(num,0) 
        # now we have a dictionary with all frequencies
        for num, cnt in count.items():
            freq[cnt].append(num) # based on count, add num to the list of th e respective freq
        res = []
        for i in range(len(freq)-1 , 0, -1): # traverse backwards bc we need max
            for num in freq[i]: # traverse sublist
                res.append(num)
                if len(res) == k:
                    return res #this is essentially break
            