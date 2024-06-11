class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        if len(nums1) < len(nums2):
            A, B = B, A
        total = len(nums1) + len(nums2)
        half = total//2

        while True:
            l=0
            r=len(A)-1
            



a=Solution()
print(a.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))