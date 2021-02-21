#https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i=0
        while True:
            if(i == len(intervals)-1):
                break
            if(intervals[i][1] >= intervals[i+1][0]):
                intervals[i][1] = max(intervals[i+1][1],intervals[i][1])
                intervals.pop(i+1)
            else:
                i+=1
        return intervals

a = Solution()
tab = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(a.merge(tab))