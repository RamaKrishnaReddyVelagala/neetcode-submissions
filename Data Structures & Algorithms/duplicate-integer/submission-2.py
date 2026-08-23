class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        frequency = {}
        duplicate = False
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
                duplicate = True
                break
        
        return duplicate

        