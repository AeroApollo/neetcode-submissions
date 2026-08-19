class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i,j]
                j += 1
            i += 1
        '''
        mapping = {} # val :index
        for i, n in enumerate(nums):
            need = target - n
            if need in mapping:
                return [mapping[need],i]
            mapping[n] = i



        
            