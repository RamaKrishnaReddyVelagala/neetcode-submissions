class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Division method:

        # product, zero_counter  = 1, 0 
        # for num in nums:
        #     if num != 0:
        #         product = product * num
        #     else:
        #         product = product 
        #         zero_counter += 1        
        # output = []
        # if zero_counter == len(nums):
        #     return [0] * zero_counter
        
        # for num in nums:
        #     if num != 0:
        #         if zero_counter >= 1:
        #             output.append(0)
        #             continue
        #         else:
        #             output.append(int(product/num))
        #             continue
        #     else:
        #         if zero_counter == 1:
        #             output.append(int(product))
        #         else:
        #             output.append(0)
        # return output


        # Method 2:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        output = [1] * n

        # Fill prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Fill suffix products
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Final output
        for i in range(n):
            output[i] = prefix[i] * suffix[i]

















