class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        arr1 = []
        arr2 = []
        for i in range(len(nums1)):
            if nums1[i] not in s2:
                arr1.append(nums1[i])
                s2.add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in s1:
                arr2.append(nums2[i])
                s1.add(nums2[i])
        return [arr1, arr2]
        