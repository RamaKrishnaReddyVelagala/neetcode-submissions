class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_counter  = 1, 0 
        for num in nums:
            if num != 0:
                product = product * num
            else:
                product = product 
                zero_counter += 1        
        output = []
        for num in nums:
            if num == 0:
                output.append(int(product))
                continue
            elif zero_counter >= 1:
                output.append(0)
            else:    
                output.append(int(product/num))
        
        return output