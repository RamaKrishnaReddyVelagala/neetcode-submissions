class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        final_list = []
        count_dic = defaultdict(int)
        for val in nums:
            count_dic[val] += 1
        my_t = list(count_dic.items())
        my_t.sort(key=lambda x: x[1], reverse=True)
        final_list = list(val[0] for val in my_t)
        return final_list[:k]