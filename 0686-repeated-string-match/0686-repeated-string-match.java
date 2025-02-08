class Solution {
    public int repeatedStringMatch(String a, String b) {

        for (int repetitions = 1; repetitions <= b.length() + 1; repetitions++) {
            StringBuilder repeatedA = new StringBuilder();

            for (int i = 0; i < repetitions; i++) {
                repeatedA.append(a);
            }

            if (repeatedA.toString().contains(b)) {
                return repetitions;
            }
        }

        return -1; 
    }
}