class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def subset(nums):
            curset, subsets = [], []
            helper(0, nums, curset, subsets)
            return subsets

        def helper(i, nums, curset, subsets):

            if i >= len(nums):
                subsets.append(curset.copy())
                return subsets
            
            # decision to include.
            curset.append(nums[i])
            helper(i + 1, nums, curset, subsets)

            curset.pop()

            #decision to not include.
            helper(i + 1, nums, curset, subsets)
        
        subsets = subset(nums)

        total = 0
        for val in subsets:
            x = 0
            for item in val:
                x ^= item
            total += x
        
        return total


        