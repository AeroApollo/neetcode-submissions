class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # here every row is increasing or ascending
        # nested binary search should make O(log(m*n))
        # challenge is to isolate the row properly bc just checking first value of row is not enough
        # we know that a target is in row i when target > matrix[i][0] and target < matrix[i][-1]
        # let's say target > matrix[i][0] and target > matrix[i][-1]: top = mid_row
        # target < matrix[i][0]:  bot = mid_row
        # three conditions should get us honed in on row
        # we should need do binary search on left right when target is in row. 
        

        top = 0
        bottom = len(matrix)-1

        #print(bottom,right)
        
        #count = 0

        while top <= bottom:
            '''
            if count > 20:
                    print("STUCK:", top, bottom, mid_row)
                    break
            count += 1
            '''
            mid_row = (top+bottom)//2
            #print(top,bottom,mid_row)
            if target < matrix[mid_row][0]: 
                #print('top')
                bottom = mid_row-1
            elif target == matrix[mid_row][0]: 
                return True
            elif target > matrix[mid_row][-1]: 
                #print('bottom')
                top = mid_row+1
            elif target == matrix[mid_row][-1]: return True
            elif target < matrix[mid_row][-1]: # target is in the row
                left = 0
                right = len(matrix[0])-1
                while left <= right:
                    mid_col = (left+right)//2
                    #print(left,right,mid_col)
                    if target < matrix[mid_row][mid_col]: right = mid_col-1
                    elif target > matrix[mid_row][mid_col]: left = mid_col+1
                    else: return True
                return False
        return False

            

        