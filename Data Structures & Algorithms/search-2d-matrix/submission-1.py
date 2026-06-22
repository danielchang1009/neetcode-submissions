class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row ,column = len(matrix) , len(matrix[0])
        top ,bot = 0 , row-1
        while bot >= top :
            mid1 = (bot+top)//2
            if matrix[mid1][-1] < target:
                top = mid1 + 1
            elif matrix[mid1][0] > target: 
                bot = mid1 - 1
            else:
                break
        if not (top<=bot):
            return False
        left , right =  0 , column-1
        while right >= left :
            mid2 = (left+right)//2
            if matrix[mid1][mid2] > target :
                right = mid2 - 1
            elif matrix[mid1][mid2] < target:
                left = mid2+1
            else:
                return True
        return False



        