class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prods[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            prods[i] *= postfix
            postfix *= nums[i]
        return prods

            