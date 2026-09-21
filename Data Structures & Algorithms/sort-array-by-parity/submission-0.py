class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        i, j = 0, len(nums) - 1
        while i < j:

            # move all even to first..

            if nums[i]%2 == 1:
                # if odd, find even from right
                if nums[j]%2 == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    j = j - 1
                    continue
            else:
                # if even
                i = i + 1
                continue
        return nums