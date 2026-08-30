class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this sounds like a binary search problem
        # start at mid
        # if target < mid: change right bound to be mid
        # else: change left bound to be mid bc target > mid
        # keep doing until target is found (while)
        l = 0
        r = len(nums)-1
        #print((l+r)//2)
        while l <= r:
            mid = (l+r)//2
            #print(mid)
            #print(nums[mid])
            if target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
            else:
                return mid
            #print(l,r)
        return -1