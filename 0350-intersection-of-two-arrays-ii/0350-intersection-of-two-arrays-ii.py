class Solution:
    def intersect(self, nums1, nums2):
        map1 = defaultdict(int)
        for num in nums1:
            map1[num] += 1
        
        result = []
        for num in nums2:
            if map1[num] > 0:
                result.append(num)
                map1[num] -= 1
        
        return result