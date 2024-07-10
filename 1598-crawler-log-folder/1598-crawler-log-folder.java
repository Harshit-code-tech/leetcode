class Solution {
    public int minOperations(String[] logs) {
        int c = 0;
        for(String s : logs){
            if(s.equals("./")){
                continue;
            }
            else if(s.equals("../")){
                if(c==0){continue;}
                else{c--;}
            }
            else{c++;}
            
        }return c;
    }
}