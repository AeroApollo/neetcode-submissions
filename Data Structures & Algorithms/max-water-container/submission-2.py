class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_h20 = 0
        i = 0; j = len(heights)-1
        while i < j:
            if heights[i] <= heights[j]:
                area = (j-i)*heights[i]
                i += 1
            else:
                area = (j-i)*heights[j]
                j -= 1
            max_h20 = max(max_h20,area)

        return max_h20