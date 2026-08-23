class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Method 1

        # final_list = []
        # count_dic = defaultdict(int)
        # for val in nums:
        #     count_dic[val] += 1
        # my_t = list(count_dic.items())
        # my_t.sort(key=lambda x: x[1], reverse=True)
        # final_list = list(val[0] for val in my_t)
        # return final_list[:k]

        # Method 2

        count = defaultdict(int)
        freq = [[] for val in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        for key, v in count.items():
            freq[v].append(key)

        top_k = list()
        for val in freq[::-1]:
            for number in val:
                top_k.append(number)
                if len(top_k) == k:
                    return top_k
        



