class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = piles[0];
        for(int i = 0;i<piles.length;i++){
            r=Math.max(r,piles[i]);
        }
        
        int m;        
        int ans = -1;
        while(l<=r){
            m = (l+r)/2; 
            if(check(piles, h,m)){
                r = m-1;
                ans = m;
            }else{
                l = m+1;
            }
        }
        return ans;
    }

    public boolean check(int[] piles, int h, int k){
        if(k ==0)return false;
        int i = 0;
        while(h>=0 && i<piles.length){

            h -=Math.ceil((double)piles[i]/k);
            i++;
        }
        return (h>=0 && i == piles.length);
    }
}