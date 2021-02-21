#https://leetcode.com/problems/rotate-image/
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        self.rotateHelper(matrix,0,len(matrix[0])-1)

    def rotateHelper(self,matrix,x,y):
        if(x == y or y <= 0): return
        h = len(matrix) - 1
        for i in range(x,y,1):
            print(matrix[x][i], matrix[i][y], matrix[y][h-i], matrix[h-i][x])
            matrix[x][i], matrix[i][y], matrix[y][h-i], matrix[h-i][x] = matrix[h-i][x], matrix[x][i], matrix[i][y], matrix[y][h-i]
        if(x == y-1): return
        self.rotateHelper(matrix,x+1,y-1)
        return

a = Solution()
mat = [[1]]
a.rotate(mat)
print(mat)