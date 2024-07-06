class Solution {
    public long countSubarrays(int[] array, int target) {
        int n = array.length;
        long total = 0;
        Map<Integer, Integer> previousResults = new HashMap<>();        
        for (int i = 0; i < n; ++i) {
            Map<Integer, Integer> currentResults = new HashMap<>();           
            if (array[i] == target) {
                ++total;
            }           
            currentResults.put(array[i], currentResults.getOrDefault(array[i], 0) + 1);          
            for (Map.Entry<Integer, Integer> entry : previousResults.entrySet()) {
                int value = entry.getKey();
                int frequency = entry.getValue();
                
                int newAndResult = value & array[i];
                
                if (newAndResult == target) {
                    total += frequency;
                }
                
                currentResults.put(newAndResult, currentResults.getOrDefault(newAndResult, 0) + frequency);
            }
            
            previousResults = currentResults;
        }
        
        return total;
    }
}
