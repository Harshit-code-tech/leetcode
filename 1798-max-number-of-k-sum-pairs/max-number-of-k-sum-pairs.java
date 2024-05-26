class Solution {
    public int maxOperations(int[] nums, int k) {
        // Check for edge cases where it's not possible to form pairs
        if(nums.length < 2 || k < 1) return 0;

        // Initialize a counter for the number of operations
        int count = 0;

        // Create a HashMap to store the frequency of each number in the array
        Map<Integer, Integer> map = new HashMap<>();
        
        // Iterate through the array
        for(int i = 0; i < nums.length; i++) {
            // Calculate the difference between the target value k and the current element
            int temp = k - nums[i];

            // Check if the difference (temp) is already present in the HashMap
            if(map.containsKey(temp)) {
                // If yes, increment the count as a pair is found
                count++;

                // If the frequency of the difference is 1, remove it from the HashMap
                if(map.get(temp) == 1) {
                    map.remove(temp);
                }
                // If the frequency is greater than 1, decrement the frequency
                else {
                    map.put(temp, map.get(temp) - 1);
                }
            }
            // If the difference is not present, add the current element to the HashMap
            else {
                map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
            }
        }
        
        // Return the total count of operations
        return count;
    }
}