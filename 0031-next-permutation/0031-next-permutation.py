class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        index = -1

        # 1️⃣ find the dip
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        # 2️⃣ if no dip found → largest permutation
        if index == -1:
            nums.reverse()
            return
        
        # 3️⃣ find element just larger than nums[index]
        for j in range(n-1, index, -1):
            if nums[j] > nums[index]:
                nums[j], nums[index] = nums[index], nums[j]
                break
        
        # 4️⃣ reverse the suffix
        left, right = index + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
