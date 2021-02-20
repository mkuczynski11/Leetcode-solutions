#https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        if(height == []): return 0
        result = 0
        tmp = [_ for _ in height]
        for x in range(1,len(tmp),1):
            if(tmp[x-1] > tmp[x]):
                tmp[x] = tmp[x-1]
        v = height[-1]
        tmp[-1] = 0
        for x in range(len(tmp) - 2, -1,-1): 
            b = 0
            if(height[x] > v):
                v = height[x]
            b = min(v,tmp[x]) - height[x]
            result += b
        return result
        '''
        result = 0
        size = len(height)
        lo = 0
        hi = size-1
        left_max = right_max = 0
        while lo < hi:
            if(height[lo] < height[hi]):
                if(height[lo] >= left_max):
                    left_max = height[lo]
                else:
                    result += left_max - height[lo]
                lo += 1
            else:
                if(height[hi] >= right_max):
                    right_max = height[hi]
                else:
                    result += right_max - height[hi]
                hi -= 1
        return result


a = Solution()
tab = [4,2,0,3,2,5]
print(a.trap(tab))