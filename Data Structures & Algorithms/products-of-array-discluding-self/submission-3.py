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
        if zero_counter == len(nums):
            return [0] * zero_counter
        
        for num in nums:
            if num != 0:
                if zero_counter >= 1:
                    output.append(0)
                    continue
                else:
                    output.append(int(product/num))
                    continue
            else:
                if zero_counter == 1:
                    output.append(int(product))
                else:
                    output.append(0)
        return output
        

                
            
        
        return output