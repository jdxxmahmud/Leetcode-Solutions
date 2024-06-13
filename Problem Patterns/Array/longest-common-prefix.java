## Problem Link: https://leetcode.com/problems/longest-common-prefix

class Solution {
    public String longestCommonPrefix(String[] strs) {

        String lcp = strs[0];

        for(int i = 1; i < strs.length; i++)
        {
            String temp = "";
            
            for(int j = 0; j < strs[i].length() && j < lcp.length(); j++)
            {
                if(strs[i].charAt(j) != lcp.charAt(j))
                    break;
                    
                temp += lcp.charAt(j);
            }

            lcp = temp;
        }

        return lcp;

        
    }
}
