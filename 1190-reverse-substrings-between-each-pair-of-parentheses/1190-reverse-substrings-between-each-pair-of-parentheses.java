class Solution {
    public String reverseParentheses(String s) {
        int len = s.length();
        if(len==0||len==1)
        return s;
        if(len==2)
        {
            if(s.charAt(0)=='(')
            {
                return "";
            }
                return s;
        }  
        String s1;
        StringBuilder s2 = new StringBuilder(s), substr;
        Stack<Integer> str = new Stack<>();
        for(int i=0;i<s2.length();i++)
        {
           Character ch = s2.charAt(i);
            if(ch=='('){
                str.push(i);
            }
            else if(ch==')'){
                int c = str.pop();
                s1 = s2.substring(c+1,i);
                substr = new StringBuilder(s1);
                s2.replace(c,i+1, substr.reverse().toString());
                i=i-2;
            }
        }
            return s2.toString();
    }
}