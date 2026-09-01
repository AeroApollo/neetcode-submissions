class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if ind 0 >= ind(len(nums)): then there are two sections. otherwise it's a sorted list
        # first we check if it's a sorted list, bc if it is then it's just binary search
        # else we need to identify where the split is to get to binary search
        # we calc mid we need to check if the mid value is in left section or right section
        # if mid value is >= left value, then we're in the left section so, left = mid +1
        # else we are in the right section so right = mid -1
        # this means that we need to check the mid value with target

        l, r = 0, len(nums)-1

        while l <= r:   
            mid = (l+r)//2
            #print(l,mid,r)
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: #we are in left section
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid -1
            else:# we are in right section
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1