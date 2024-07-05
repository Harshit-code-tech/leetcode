class Solution {
    public int[] searchRange(int[] nums, int target) {

        int[] ans = new int[2];
        if(nums.length == 0)
        {
            ans[0] = -1;
            ans[1] = -1;
            return ans;
        }
       
        for(int i = 0; i < nums.length; i++)
        {
            for(int j = nums.length-1; j >= i; j--)
            {
                if(nums[i] == target && nums[j] == target)
                {   ans[0] = i;
                    ans[1] = j;
                    return ans;
                }
            }
        }
       
        ans[0] = -1;
        ans[1] = -1;
        return ans;
    }
}