class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        width = len(matrix[0])
        height = len(matrix)
        l, r = 0, (width*height-1)
        while l < r:
            mid = (l + r // 2)
            if matrix[mid//width][mid%width] < target:
                l = mid +1
            else:
                r = mid
        return matrix[l//width][l%width] == target
    
a=Solution()

print(a.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 12))