class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # pos={}
        # sum_t=0
        # for i, num in enumerate(nums):
        #     if num not in pos:
        #         positi=[i,num]
        #         positi.append(pos)
        #     for j in range(i):
        #         if i in pos:
        #             sum_t[i]+=abs(i.value-j.value)
        #     if num in pos<1:
        #         sum_t[i]
        # return sum_t[i]
        group={}
        for i, num in enumerate(nums):
            if num not in group:
                group[num]=[]
            group[num].append(i)
        print(group)
        # return[]
        ans=[0]*len(nums)
        # for indices in group.values():
        #     for i in indices:
        #         total_dis=0
        #         for j in indices:
        #             total_dis+=abs(i-j)
        #         ans[i]=total_dis
        # return ans
        for indices in group.values():
            left_count=0
            left_sum=0
            for i in indices:
                ans[i]=(left_count*i)-left_sum
                left_count+=1
                left_sum+=i
            right_count=0
            right_sum=0
            for i in reversed (indices):
                ans[i]+=right_sum-(right_count*i)
                right_count+=1
                right_sum+=i
        return ans

        
