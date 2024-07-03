class Solution {
    public int minDifference(int[] nums) {
        if(nums.length<=4){
            return 0;
        }
        Arrays.sort(nums);
        int l=nums.length;
        int min1=Math.min(nums[l-1]-nums[3],nums[l-2]-nums[2]);
        int min2=Math.min(nums[l-3]-nums[1],nums[l-4]-nums[0]);
        int min3=Math.min(min1,min2);
       return min3;
    }
}
