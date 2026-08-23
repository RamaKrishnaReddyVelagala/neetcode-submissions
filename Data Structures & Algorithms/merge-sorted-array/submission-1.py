class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = r = 0

        for l in range(len(nums1)):
            if nums1[l] == 0 and r < len(nums2):
                nums1[l] = nums2[r]
                r += 1

        nums1.sort()        