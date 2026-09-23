class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curset, subsets = [], []


        def helper(i, nums, curset, subsets):

            if i>=len(nums):
                subsets.append(curset.copy())
                return
            
            # to include
            curset.append(nums[i])
            helper(i+1, nums, curset, subsets)
            curset.pop()

            # to not include

            helper(i+1, nums, curset, subsets)
        helper(0, nums, curset, subsets)
        return subsets