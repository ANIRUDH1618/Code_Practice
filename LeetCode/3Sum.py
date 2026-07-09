class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j==i:
                    continue
                for k in range(len(nums)):
                    if k==i or k==j:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])

        return res
