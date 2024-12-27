class Solution {
    public int romanToInt(String s) {
        Map<Character,Integer> romanMap= new HashMap<>();
        romanMap.put('I',1);
        romanMap.put('V',5);
        romanMap.put('X',10);
        romanMap.put('L',50);
        romanMap.put('C',100);
        romanMap.put('D',500);
        romanMap.put('M',1000);
        
        int result =0;
        for(int i =0;i<s.length();i++){
            int curr=romanMap.get(s.charAt(i));
            int next =(i<s.length()-1) ? romanMap.get(s.charAt(i+1)):0;
            if(curr<next){
                result-=curr;

            }
            else{
                result+=curr;
            }

        }
        return result;

        
    }
}