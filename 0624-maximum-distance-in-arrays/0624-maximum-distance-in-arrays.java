class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        int minVal = arrays.get(0).get(0);
        int maxVal = arrays.get(0).get(arrays.get(0).size() - 1);
        int maxDistance = 0;

        for (int i = 1; i < arrays.size(); i++) {
            List<Integer> currentArray = arrays.get(i);
            int currentMin = currentArray.get(0);
            int currentMax = currentArray.get(currentArray.size() - 1);

            // Calculate distances and update maxDistance
            maxDistance = Math.max(maxDistance, Math.abs(maxVal - currentMin));
            maxDistance = Math.max(maxDistance, Math.abs(currentMax - minVal));

            // Update global minVal and maxVal
            minVal = Math.min(minVal, currentMin);
            maxVal = Math.max(maxVal, currentMax);
        }

        return maxDistance;
    }
}