class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        int n=names.length;
        Map<Integer,String> map = new HashMap<>();
        for(int i=0;i<n;i++){
            map.put(heights[i],names[i]);
        }
        Arrays.sort(heights);
        revArr(heights);
        for(int i=0;i<n;i++){
            names[i] = map.get(heights[i]);
        }
        return names;
    }

    static void revArr(int[] arr){
        int left=0;
        int right = arr.length-1;
        while(left<right){
            int temp = arr[left];
            arr[left] =arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
}