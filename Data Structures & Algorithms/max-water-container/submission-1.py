class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0; j = len(heights)-1
        maxArea = 0
        while i < j:
            width = j-i
            curr_Area = min(heights[i],heights[j])*width
            if curr_Area > maxArea:
                maxArea = curr_Area
                #print([i,j])
            # if the next height is taller than current i or j, then can store more area
            # if we inc or dec, width always decreases.
            # since width always decreases, to find a new maxArea we must move the smaller height to a new height bc other it will always shrink
            if heights[i]<heights[j]:
                i += 1
            else:
                j -= 1

        return maxArea


        