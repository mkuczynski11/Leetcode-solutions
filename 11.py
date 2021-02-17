#https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, maxA = 0,len(height) - 1, 0
        while left != right:
            area = min(height[left], height[right])*(right-left)
            if(area > maxA): maxA = area
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return maxA