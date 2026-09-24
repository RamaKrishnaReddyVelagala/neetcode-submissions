class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        currset, result = [], []

        def helper(i, currset, total):
            if target == total:
                result.append(currset.copy())
                return

            if i>= len(candidates) or total > target:
                return
            
            # decision to include
            currset.append(candidates[i])
            helper(i + 1, currset, sum(currset))
            currset.pop()

            #decision to not include
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, currset, sum(currset))
        helper(0, [], 0)
        return result
