class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Method 1: using dicitonary - use tuple on dict .items() also the key need to be adjusted so see.
        
        # def word_count(a):
        #     a_dic = {}
        #     for val in a:
        #         a_dic[val] = a_dic.get(val, 0) + 1
        #     return a_dic
        # # i can also use tuple(dict.items()) - python >=3.7 we have them as equals
        # main_dic = {}
        # for val in strs:
        #     if tuple(sorted(word_count(val).items())) not in main_dic:
        #         main_dic[tuple(sorted(word_count(val).items()))] = [val]
        #     else:
        #         main_dic[tuple(sorted(word_count(val).items()))].append(val)
            
        # return list(main_dic.values())
            
        
        # Method 2: using ord

        main_dic = defaultdict(List)
        for val in strs:
            my_list = [0] * 26
            for char in val:
                char[ord(val) - ord(a)] += 1
            
            main_dic[tuple(char[ord(val) - ord(a)])].append(val)

        return list(main_dic.values())





