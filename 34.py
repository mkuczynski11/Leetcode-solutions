#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(not len(nums)): return [-1,-1]
        lo = 0
        hi = len(nums) - 1
        i_lo = 0
        while hi > lo:
            i = (hi + lo)//2
            if(nums[i] > target):
                hi = i-1
            elif(nums[i] < target):
                lo = i+1
            else:
                hi = i
        if(nums[hi] != target): return [-1,-1]
        i_lo = hi
        hi = len(nums) - 1
        while hi > lo:
            i = (hi + lo)//2
            if(nums[i] > target):
                hi = i-1
            elif(nums[i + 1] == target):
                lo = i+1
            else:
                lo = i
                break
        return [i_lo, lo]
        
a = Solution()
print(a.searchRange([1], 1))