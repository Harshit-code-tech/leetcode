class Solution {
public:
    bool validPalindrome(string s) {
        bool pal = false;
        int n = s.size();

        for(int i = 0; i < n; i++){
            string str = "";
            str = s.substr(0, i);
            if( i + 1 < n){
                str += s.substr(i + 1);
            }

            string check = str;
            reverse(check.begin(), check.end());

            if(check == str){
                return true;
            }
        }

        return false;
    }
};