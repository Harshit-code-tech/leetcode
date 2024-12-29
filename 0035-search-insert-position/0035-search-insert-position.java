class Solution {
    public int searchInsert(int[] nums, int target) {
        if (nums.length == 0) {
            return 0; 
        }
        int l=0;
        int r =nums.length-1;
        while(l<=r){
            int mid = l+(r-l)/2;
            if(nums[mid]==target){
                return mid;
            }else if(nums[mid]<target){
                l=mid+1;
            }else{
                r= mid-1;
            }
        }
        return l;
        
    }
}