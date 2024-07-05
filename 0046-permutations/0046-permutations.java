class Solution {
    public List<List<Integer>> permute(int[] nums) {

        List<List<Integer>> list = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();

        if (nums.length == 0)
            return list;

        util(nums, nums.length, list, temp);
        return list;

    }

    void util(int[] nums, int n, List<List<Integer>> list, List<Integer> temp) {

        if (temp.size() == n) {
            list.add(new ArrayList<>(temp));
            return;
        }

        for (int num : nums) {
            if (!temp.contains(num)) {
                temp.add(num);
                util(nums, n, list, temp);
                temp.removeLast();

            }
        }
        return;
    }
}