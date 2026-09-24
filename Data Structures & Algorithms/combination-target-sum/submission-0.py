class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        currset = []

        def helper(i, currset, total):

            if total == target:
                result.append(currset.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            # to include or not to include.
            currset.append(nums[i])
            
            helper(i, currset, total=sum(currset))
            currset.pop()
            
            # to not include
            helper(i + 1, currset, total=sum(currset))
        helper(0, [], 0)

        return result


