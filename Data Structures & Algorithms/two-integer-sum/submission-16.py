class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # start with ind i rep a number
        # instead of traversing through list with j which makes O(N^2)
        # we can set a number we are looking for target-nums[i] 
        # and check if that target is in the rest of list
        seen = []
        i = 0
        while i < len(nums):
            find = target-nums[i]
            if find in seen:
                j = seen.index(find)
                #print('found',i,j,find,find not in nums[i+1:])
                break     
            else:
                seen.append(nums[i])
            i += 1
        print(i,j)
        if i < j: return [i,j]
        return [j,i]