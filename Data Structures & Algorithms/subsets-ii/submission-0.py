class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currset, subset = [], []
        
        def helper(i, currset, subset, nums):

            if i >= len(nums):
                subset.append(currset.copy())
                return
            
            # decision to include.
            currset.append(nums[i])
            helper(i + 1, currset, subset, nums)
            currset.pop()

            # decision to not include
            while i + 1 < len(nums):
                if nums[i] == nums[i + 1]:
                    i = i + 1
                    continue
                break
            helper(i + 1, currset, subset, nums)
        helper(0, currset, subset, nums)

        return subset
