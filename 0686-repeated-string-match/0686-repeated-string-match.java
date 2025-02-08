class Solution {
   public int repeatedStringMatch(String A, String B) {
        
        
        char[] a = A.toCharArray();
        char[] b = B.toCharArray();
        for(int i=0;i<a.length;i++){
            int len = loop(a,b,i);
            if(len > 0){// 
                int count = 1;
                
                len = B.length() - a.length + i;
                count += len/a.length;
                count += len%a.length > 0 ? 1 : 0;
                return count;
            }else if(len + a.length <= 0){
                return -1;
            }
        }
        return -1;
        
    }
    public int loop(char[] a,char[] b,int start){
        int count = start;
        for(char c : b){
            if(a[start % a.length] != c){
                return count - start;
            }
            start++;
        }
        return 1; 
    }
}