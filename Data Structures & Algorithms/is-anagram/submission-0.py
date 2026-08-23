class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def word_counter(s: str):
            my_dic = {}
            for char in s:
                if char in my_dic:
                    my_dic[char] += 1
                    continue
                my_dic[char] = 0
            return my_dic
        
        if word_counter(s) == word_counter(t):
            return True
        return False

        