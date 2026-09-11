class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        set_nums = set()
        for num in nums:
            if num not in set_nums:
                set_nums.add(num)
        sort_set = sorted(set_nums)
        longest = 1
        #print(sort_set)
        i = 1
        curr_len = 1
        while i < len(sort_set):
            if sort_set[i]-sort_set[i-1] == 1:
                curr_len += 1
            else:
                curr_len = 1
            if curr_len > longest:
                longest = curr_len
            i += 1
            #print(curr_len)
        return longest
