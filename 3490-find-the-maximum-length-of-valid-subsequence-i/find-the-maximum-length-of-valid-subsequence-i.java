class Solution {
    public int countValidSubsequence(List<Integer> nums) {
        int counterEvenSum = 0, counterOddSum = 1, counterEven = 2, counterOdd = 3;
        int[] counters = new int[4];
        boolean[] parityFlags = {true, false};

        for (int num : nums) {
            int parity = num % 2;
            if ((parity == 1 && !parityFlags[counterOddSum]) || (parity == 0 && parityFlags[counterOddSum])) {
                parityFlags[counterOddSum] = !parityFlags[counterOddSum];
                counters[counterOddSum]++;
            }
            
            if ((parity == 1 && !parityFlags[counterEvenSum]) || (parity == 0 && parityFlags[counterEvenSum])) {
                parityFlags[counterEvenSum] = !parityFlags[counterEvenSum];
                counters[counterEvenSum]++;
            }
            
            if (parity == 1) {
                counters[counterOdd]++;
            }
            if (parity == 0) {
                counters[counterEven]++;
            }
        }
        return Arrays.stream(counters).max().orElse(0);
    }

    public int maximumLength(int[] nums) {
        List<Integer> numsList = new ArrayList<>();
        for (int num : nums) {
            numsList.add(num);
        }
        return countValidSubsequence(numsList);
    }
}
