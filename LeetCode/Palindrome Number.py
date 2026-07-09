class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = str(x)
        b = str(a)[::-1]

        if a == b:
            return  True
        else:
            return False