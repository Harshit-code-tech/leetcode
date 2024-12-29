class Solution {
    public int lengthOfLastWord(String s) {
        int end = s.length() - 1;
        while (end >= 0 && s.charAt(end) == ' ') {
            end--; 
        }
        int l=0;
        for(int i =end;i>=0;i--){
            if(s.charAt(i)!=' '){
                l++;
            }else{
                break;
            }
        }
        return l;
        
    }
}