public class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int count = 0;
        // Use a hash table to store the prefix sum remainders and their frequencies
        Map<Integer, Integer> remainderCount = new HashMap<>();

        // Initialize remainderCount with 1 for remainder 0 (empty subarray)
        remainderCount.put(0, 1);

        int sum = 0;
        for (int num : nums) {
            // Add current element to the sum
            sum += num;

            // Handle negative remainders (Java % for negative numbers can be tricky)
            int remainder = sum % k;
            if (remainder < 0) {
                remainder += k; // Make sure remainder is non-negative
            }

            // Check if a previous subarray with the same remainder exists
            if (remainderCount.containsKey(remainder)) {
                count += remainderCount.get(remainder);
            }

            // Update frequency of the current remainder
            remainderCount.put(remainder, remainderCount.getOrDefault(remainder, 0) + 1);
        }

        return count;
    }
}
