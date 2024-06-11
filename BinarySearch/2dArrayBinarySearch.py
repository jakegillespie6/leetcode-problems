class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top, bot = 0, ROWS-1

        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][COLS-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not top<=bot:
            return False
        l, r = 0, COLS-1
        while l<=r:
            mid = (l+r)//2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False
            
a=Solution()
print(a.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 11))
