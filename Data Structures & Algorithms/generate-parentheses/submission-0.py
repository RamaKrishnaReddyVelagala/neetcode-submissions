class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        p, c, curset, subsets = 0, 0, [], []

        def helper(p, c, curset, subsets):
            if len(curset) == 2 * n:
                subsets.append("".join(curset))
                return

            # add open bracket only if open < n
            if p < n:
                curset.append("(")
                helper(p + 1, c, curset, subsets)
                curset.pop()

            # add close bracket only if closed < open
            if c < p:
                curset.append(")")
                helper(p, c + 1, curset, subsets)
                curset.pop()

        helper(0, 0, curset, subsets)
        return subsets