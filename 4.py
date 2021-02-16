class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        imin = 0
        imax = m
        median = (m+n+1)/2
        while imin <= imax :
            i = (imin + imax)/2
            j = median - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    lmin = nums2[j-1]
                elif j == 0:
                    lmin = nums1[i-1]
                else:
                    lmin = max(nums2[j-1], nums1[i-1])

                if (m + n) % 2 == 1:
                    return lmin

                if i == m:
                    lmax = nums2[j]
                elif j == n:
                    lmax = nums1[i]
                else:
                    lmax = min(nums2[j],nums1[i])
                return (lmin + lmax) / 2.0