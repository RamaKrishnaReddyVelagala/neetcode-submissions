class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            mid = (l + r)//2
            print("mid:",mid)
            print(mid * mid)

            if (mid * mid) < x:
                l = mid + 1
                print("l:",l)
            elif (mid * mid) > x:
                r = mid - 1
                print("r:",r)
            else:
                return mid

        return l-1
        