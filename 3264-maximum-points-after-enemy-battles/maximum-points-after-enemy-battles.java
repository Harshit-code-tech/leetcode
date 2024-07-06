class Solution {
    public long maximumPoints(int[] enemyEnergies, int currentEnergy) {
        Arrays.sort(enemyEnergies);        
        if (currentEnergy < enemyEnergies[0]) {
            return 0;
        }        
        long totalPoints = 0;
        int n = enemyEnergies.length;
        int element = enemyEnergies[0];        
        if (n == 1) {
            return currentEnergy / element;
        }       
        for (int i = n - 1; i > 0; i--) {
            currentEnergy += enemyEnergies[i];
            long increment = currentEnergy / element;
            totalPoints += increment;
            currentEnergy %= element;
        }       
        return totalPoints;
    }
}