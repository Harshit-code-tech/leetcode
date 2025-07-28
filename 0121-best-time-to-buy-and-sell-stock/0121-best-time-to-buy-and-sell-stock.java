class Solution {
    public int maxProfit(int[] prices) {
        int minPrice=prices[0];
        int maxprofit=0;
        int profit=0;
        for( int i =1; i<prices.length;i++){
            minPrice=Math.min(prices[i],minPrice);
            profit = prices[i]-minPrice;
            maxprofit=Math.max(maxprofit,profit);
        }
        return maxprofit;
    }
}