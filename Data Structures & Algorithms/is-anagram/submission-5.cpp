class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        unordered_map<char,int> countsS;
        unordered_map<char, int> countsT;

        for (int i = 0; i < s.length(); i++){
            countsS[s[i]] += 1;
            countsT[t[i]] += 1;
        }
        
        return countsS == countsT;
        
    }
};
