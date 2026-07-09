class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        d = arr[1] - arr[0]
        for i in range(len(arr)):
            if arr[i+1] == d + arr[i]:
                continue
            else:
                return False
            
        return True