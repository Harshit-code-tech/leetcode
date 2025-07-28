class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> table = new HashSet<>();
        for(int n:nums){
            if(table.contains(n))
            return true;
            else table.add(n);
        }
        return false;     
    }
}