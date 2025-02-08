class Solution {
    public int repeatedStringMatch(String a, String b) {
        int count=1;

        StringBuilder sb=new StringBuilder(a);
        while(sb.length()<b.length()){
            count++;
            sb.append(a);
        }
        if(sb.indexOf(b)>=0)return count;
        if(sb.append(a).toString().contains(b)) return count+1;
        return -1;
    }
}