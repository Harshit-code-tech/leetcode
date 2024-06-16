class Solution {
    public long maximumTotalDamage(int[] power) {
        Map<Integer, Integer> damageFrequency = new HashMap<>();
        for (int damage : power) {
            damageFrequency.put(damage, damageFrequency.getOrDefault(damage, 0) + 1);
        }

        List<Integer> uniqueDamages = new ArrayList<>(damageFrequency.keySet());
        Collections.sort(uniqueDamages);
        int n = uniqueDamages.size();
        if (n == 0) return 0;

        long[] dp = new long[n];
        dp[0] = (long) uniqueDamages.get(0) * damageFrequency.get(uniqueDamages.get(0));
        for (int i = 1; i < n; i++) {
            long currentDamage = (long) uniqueDamages.get(i) * damageFrequency.get(uniqueDamages.get(i));
            dp[i] = currentDamage;
            int j = i - 1;
            while (j >= 0 && uniqueDamages.get(i) - uniqueDamages.get(j) <= 2) {
                j--;
            }
            if (j >= 0) {
                dp[i] += dp[j];
            }
            dp[i] = Math.max(dp[i], dp[i - 1]);
        }

        return dp[n - 1];
    }
}
