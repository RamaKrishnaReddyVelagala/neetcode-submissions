class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Method1: set
        # if len(set(nums)) != len(nums):
        #     return True
        # return False

        # Method2: dic
        my_dic = {}
        for val in nums:
            if val in my_dic:
                return True
            my_dic[val] = 0
        return False

