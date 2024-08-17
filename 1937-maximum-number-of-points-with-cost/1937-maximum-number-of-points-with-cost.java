class Solution {
    public long maxPoints(int[][] points) {
        int m = points.length;
        int n = points[0].length;
        long dp [][] = new long [m][n];
        for(int i=0;i<n;i++){
          dp[0][i] = points[0][i];
        }
        for(int i=1;i<m;i++){
          for(int j=0;j<n;j++){
            dp[i][j] = points[i][j];
            long maxPoints = 0;
            for(int k=0;k<n;k++){
              maxPoints = Math.max(maxPoints,(dp[i-1][k] - Math.abs(k-j)));
            }
            dp[i][j] += maxPoints;
          }
        }
        long ans = 0;
        for(int i=0;i<n;i++){
          ans = Math.max(dp[m-1][i],ans);
        }
    
        return ans ;
    }
}