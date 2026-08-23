class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n = min(len(word1), len(word2))
        merged_string = ""
        # for i in range (0, n):
        #     if len(word1) == len(word2):
        #         merged_string

        for l in range(0, n):
            merged_string = merged_string + word1[l]
            merged_string = merged_string + word2[l]

        if len(word1) > n:
            merged_string = merged_string + word1[n:]
        elif len(word2) > n:
            merged_string = merged_string + word2[n:]
    
        return merged_string


    