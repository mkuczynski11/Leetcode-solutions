#https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums.sort()
        #for i in range(0,len(nums)-1,2):
        #    if(i == len(nums) - 3 and nums[i] == nums[i+1]):return nums[i+2]
        #    elif(nums[i] == nums[i+1]): continue
        #    else: return nums[i]
        #return nums[0]
        s = set()
        for i in range(len(nums)):
            if(nums[i] in s): s.remove(nums[i])
            else: s.add(nums[i])
        return s.pop()