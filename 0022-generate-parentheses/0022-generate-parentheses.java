class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        generateCombinations(result, "", n, 0, 0);
        return result;
    }

    private void generateCombinations(List<String> result, String currentString, int n, int openCount, int closeCount) {
        if (openCount == n && closeCount == n) {
            result.add(currentString);
            return;
        }

        if (openCount < n) {
            generateCombinations(result, currentString + "(", n, openCount + 1, closeCount);
        }

        if (closeCount < openCount) {
            generateCombinations(result, currentString + ")", n, openCount, closeCount + 1);
        }
    }
}
