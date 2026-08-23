class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        for op in operations:
            if op == 'D':
                nums.append(nums[-1] * 2)
            elif op == 'C':
                nums.pop()
            elif op == '+':
                nums.append(nums[-2] + nums[-1])
            else:
                nums.append(int(op))

        return sum(nums)
        