class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0; j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] < target: #if calc sum is too small even with largest num then we must inc the smallest number
                i +=1 
            #otherwise the sum is too large so we must dec largest number
            else:
                j -=1