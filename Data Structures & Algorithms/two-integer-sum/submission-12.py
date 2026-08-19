class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {} # val :index
        for i, n in enumerate(nums):
            need = target - n
            if need in mapping:
                return [mapping[need],i]
            mapping[n] = i  
            