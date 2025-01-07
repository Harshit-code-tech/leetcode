class Solution {
    public List<String> stringMatching(String[] words) {
        List<String> result = new ArrayList<>();
        Arrays.sort(words, Comparator.comparingInt(String::length)); // Sort words by length

        for (int i = 0; i < words.length; i++) {
            for (int j = i + 1; j < words.length; j++) { // Only check for longer words
                if (words[j].contains(words[i])) {
                    result.add(words[i]);
                    break; 
                }
            }
        }

        return result;
    }
}