class Solution {
    public int numberOfAlternatingGroups(int[] arr, int k) {
        int num_found = 0;
        int i = 0, j = 1;
        int n = arr.length;       
        while (j < n + k && i < n) {
            int temp_j = j;
            int temp_end = temp_j % n;
            while (arr[temp_end] != arr[(temp_end - 1 + n) % n] && temp_j < (n + k - 1)) {
                temp_j++;
                temp_end = temp_j % n;
            }
            num_found += Math.max(temp_j - i - k + 1, 0);
            i = temp_j;
            j = i + 1;
        }
        
        return num_found;
    }
}
