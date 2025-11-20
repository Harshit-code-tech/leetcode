class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums)-1
        # j=0
        # pos=0
        # count=0
        # for i in range(len(nums)):
        #     if nums[i]<0:
        #         j=nums[i]
        #         pos=nums[i]-j
        #         if nums[pos] == nums[left] | nums[right]:
        #             count+=1
        #     if nums[i]>0:
        #         j=nums[i]
        #         pos=nums[i]+jn
        #         if nums[pos] == ums[left] | nums[right]:
        #             count+=1
        # return count


        # curr_pos=0
        # count=0
        # for step in nums:
        #     if nums[curr_pos]<0:
        #         # nums[curr_pos]-=nums[curr_pos]
        #         steps=nums[curr_pos]
        #         nums[curr_pos]-=steps
        #     elif nums[curr_pos]>0:
        #         # nums[curr_pos]+=nums[curr_pos]
        #         steps=nums[curr_pos]
        #         nums[curr_pos]+=steps
        #     if curr_pos==0:
        #         count+=1
        # return count

        curr_pos=0
        count=0
        for step in nums:
            curr_pos+=step
            if curr_pos==0:
                count+=1
        return count