class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = len(nums) - 1

        while l <= r:
            if nums[l] not in nums[:l]:
                l += 1
            else:
                nums[l:r] = nums[l+1:r+1]
                r -= 1
        return l
