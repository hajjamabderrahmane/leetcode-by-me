class Solution:
    def findMedianSortedArrays(self, nums1 list[int], nums2 list[int]) - float
        nums = sorted(nums1 + nums2)
        n= len(nums)
        return ( nums[n2] + nums[(n2)-1] ) 2 if n % 2 == 0 else nums[(n-1)2]
