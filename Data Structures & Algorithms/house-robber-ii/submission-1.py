class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def r1(array):

            rob1, rob2 = 0,0

            for num in array:
                tmp = max(rob1+num,rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2

        return max(nums[0],r1(nums[:-1]),   r1(nums[1:]))