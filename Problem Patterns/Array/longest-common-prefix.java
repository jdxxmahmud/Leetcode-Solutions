## Problem Link: https://leetcode.com/problems/longest-common-prefix

class Solution {
    public String longestCommonPrefix(String[] strs) {

        String res = "";

        Arrays.sort(strs);

        int i = 0, j = 0, sz = strs.length;

        while(i < strs[0].length() && j < strs[sz - 1].length())
        {
            if (strs[0].charAt(i) == strs[sz - 1].charAt(j))
            {
                res += strs[0].charAt(i);
            }
            else
            {
                break;
            }

            i++; j++;
        }


    return res;

    }

}
