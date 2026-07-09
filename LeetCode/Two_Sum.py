class Solution:
    def __init__(self):
        pass
    
    def twoSum(self, arr, target_sum):
        seen = {}

        for i in range(len(arr)):
            complement = target_sum - arr[i]
            if complement in seen:
                return (seen[complement], i)
            seen[arr[i]] = i 


def main():
    arr = [2, 7, 11, 15]
    target = 9
    res = Solution().twoSum(arr, target)
    print(res)

if __name__ == "__main__":
    main()
