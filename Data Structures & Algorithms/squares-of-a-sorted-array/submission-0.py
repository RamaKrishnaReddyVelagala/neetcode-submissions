class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # first index with a non-negative value (n if all negative)
        mid = n
        for k in range(n):
            if nums[k] >= 0:
                mid = k
                break

        i, j = mid - 1, mid      # i walks left through negatives, j walks right
        result = []

        while i >= 0 and j < n:
            if nums[i] ** 2 < nums[j] ** 2:
                result.append(nums[i] ** 2)
                i -= 1
            else:
                result.append(nums[j] ** 2)
                j += 1

        while i >= 0:
            result.append(nums[i] ** 2)
            i -= 1
        while j < n:
            result.append(nums[j] ** 2)
            j += 1

        return result