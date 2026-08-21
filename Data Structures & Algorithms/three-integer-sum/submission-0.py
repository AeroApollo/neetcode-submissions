class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        
        res = []
        for i in range(len(nums)): # this is best bc O(N^2) is allowed.
            if i > 0 and nums[i] == nums[i-1]:
                continue # skips duplicates because not need
            need = -nums[i] # now it just becomes two pointer technique
            j = i+1; k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == need:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j +=1 
                    while j < k and nums[k] == nums[k+1]:
                        k -=1
                elif nums[j] + nums[k] < need:
                    j+=1
                else:
                    k -= 1
        return res
