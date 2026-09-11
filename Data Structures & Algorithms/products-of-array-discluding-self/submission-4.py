class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1]*len(nums)
        prefix = 1 #bc we start at leftmost and 1 wouldn't change anth
        for i in range(len(nums)):
            prods[i] *= prefix
            prefix *= nums[i] # 1 * prevnums * currnums
        postfix = 1
        for i in range(len(nums)-1,-1,-1): #from back to front
            prods[i] *= postfix
            postfix *= nums[i]
        return prods