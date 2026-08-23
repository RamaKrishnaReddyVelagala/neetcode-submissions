class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 2 loops - first check - l[0] , r[-1], then if goodinner loop binary search

        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r)//2

            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l, r = 0, len(matrix[mid]) - 1
                

                while l <=r:
                    mid_2 = (l + r)//2
                    if target > matrix[mid][mid_2]:
                        l = mid_2 + 1
                    elif target < matrix[mid][mid_2]:
                        r = mid_2 -1
                    else:
                        return True

                return False
        
        return False