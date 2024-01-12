class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> found_chars;
        int start = -1;
        int max_len = 0;

        for (int i = 0; i < s.length(); ) {
            if (found_chars.count(s[i]) == 0) {
                found_chars[s[i]] = i;
                max_len = max(max_len, i - start);
                i++;
            } else {
                if (start < found_chars[s[i]]) {
                    start = found_chars[s[i]];
                }
                found_chars.erase(s[i]);
            }
        }

        return max_len;
    }
};