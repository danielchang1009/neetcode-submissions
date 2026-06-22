class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix), len(matrix[0])
        top , bot = 0 , rows-1 
        while bot >= top:
            mid1= (top+bot)//2
            if  target > matrix[mid1][-1]:
                top = mid1 + 1
            elif target < matrix[mid1] [0]:
                bot = mid1 - 1
            else:
                break
        if not (top<=bot):
                return False 
        mid1= (top+bot) // 2
        left , right =0 ,cols-1
        while  right >=left:
            mid= (left+right) // 2
            if target > matrix[mid1][mid]:
                left= mid+1
            elif target < matrix[mid1][mid]:
                right= mid-1
            else:
                return True
        return False 
