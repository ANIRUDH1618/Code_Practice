import math

class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = x*(-1)
        
        b = int(str(x)[::-1])

        if neg:
            b = b*(-1)

        if -math.pow(2,31) <= b <= math.pow(2,31) - 1:
            return b
        else:
            return 0