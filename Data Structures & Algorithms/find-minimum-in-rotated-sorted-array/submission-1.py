class Solution:
    def findMin(self, nums: List[int]) -> int:
        # len(nums) in comparison of the first number should get you how much it's been rotated
        #n = len(nums)
        #return nums[n-nums[0]+1]
        '''
        l = 0; r = len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                r -= 1
            elif nums[l] > nums[r]:
                l += 1
            else: 
                return nums[l]
        '''
        res = nums[0]
        l , r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]: #then our section is a sorted array
                res = min(res,nums[l])
                break
            # find mid
            mid = (l+r)//2 
            res = min(res,nums[mid])
            if nums[mid] >= nums[l]: # then we are in the left section
                l = mid + 1
            else:
                r = mid -1

        return res