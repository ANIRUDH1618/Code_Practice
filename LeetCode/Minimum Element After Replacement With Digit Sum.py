class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        str_lst = [str(item) for item in nums]
        min_sum = float("inf")

        def sum_int(num):
            sum = 0

            for i in range(len(num)):
                x = int(num[i])
                sum = sum + x
            return sum

        for i in range(len(str_lst)):
            current_sum = sum_int(str_lst[i])
            
            if current_sum < min_sum:
                min_sum = current_sum
            
            nums[i] = current_sum

        return min_sum
