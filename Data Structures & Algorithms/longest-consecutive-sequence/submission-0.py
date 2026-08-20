class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in set_nums: #this means num is a start of seq
                length = 0
                while num+length in set_nums:
                    length += 1 
                longest = max(length,longest)
        return longest

