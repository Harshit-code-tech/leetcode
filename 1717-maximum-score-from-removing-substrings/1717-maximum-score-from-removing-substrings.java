class Solution {
    public int maximumGain(String s, int x, int y) {
        if (x < y) {
            int temp = x;
            x = y;
            y = temp;
            s = s.replace("a", "#").replace("b", "a").replace("#", "b");
        }

        Stack<Character> st = new Stack<>();
        int sum = 0;

        for (char ch : s.toCharArray()) {
            if (!st.isEmpty() && st.peek() == 'a' && ch == 'b') {
                st.pop();
                sum += x;
                System.out.println(sum);
            } else {
                st.push(ch);
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!st.isEmpty()) {
            sb.append(st.pop());
        }
        s = sb.reverse().toString();

        for (char ch : s.toCharArray()) {
            if (!st.isEmpty() && st.peek() == 'b' && ch == 'a') {
                st.pop();
                sum += y;
                System.out.println(sum);
            } else {
                st.push(ch);
            }
        }
        return sum;
    }
}