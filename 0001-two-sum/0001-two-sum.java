class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        int[] result = new int[2]; 

        for (int i = 0; i < len; i++) {
            for (int j = i + 1; j < len; j++) { 
                int sum = nums[i] + nums[j]; 
                if (sum == target) {
                    result[0] = i;
                    result[1] = j;
                    return result; 
                }
            }
        }
        return new int[]{};
    }
}