class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the brute for way i would do this is create a hashmap or dictionary to keep track of counts
        # then sort by values descending and return the first k values
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        sorted_counts = sorted(counts.items(),key=lambda  x:(-x[1],x[0])     )
        #print(sorted_counts)
        output = []
        i = 0
        for key,value in sorted_counts:
            if i == k:
                break
            output.append(key)
            i += 1
        return output