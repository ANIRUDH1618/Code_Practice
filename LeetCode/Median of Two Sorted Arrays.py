class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        j, k = 0,0
        res = []

        while j < len(nums1) and k < len(nums2):
            if nums1[j] >= nums2[k]:
                res.append(nums2[k])
                k += 1
            else:
                res.append(nums1[j])
                j += 1
            
        if j == len(nums1):
            for i in range(k, len(nums2)):
                res.append(nums2[i])
        else:
            for i in range(j, len(nums1)):
                res.append(nums1[i])
        
        if len(res) % 2 == 0:
            return float((res[len(res) // 2] + res[len(res) // 2 - 1]) / 2)
        else:
            return float(res[len(res) // 2])
