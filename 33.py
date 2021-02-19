#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        pivot, v_p = self.findPivot(nums, 0, hi)
        if(target < nums[0]):
            lo = pivot
        else:
            if(not pivot == 0):
                hi = pivot
        while hi >= lo:
            i = (lo + hi)//2
            if(nums[i] == target):
                return i
            elif(nums[i] < target):
                lo = i+1
            elif(nums[i] > target):
                hi = i-1
        return -1

    def findPivot(self, nums, left, right):
        i = (left + right)//2
        if(left == right):
            return left,nums[left]
        else:
            x, v_x = self.findPivot(nums, left, i)
            y, v_y = self.findPivot(nums, i+1, right)
            if(v_x < v_y):
                return x, v_x
            return y, v_y

a = Solution()
print(a.search([1,3],3))