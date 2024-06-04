// Problem Link: https://leetcode.com/problems/length-of-last-word

class Solution {
    public int lengthOfLastWord(String s) {

        // Space = O(1)
        // Time = O(n)
        
        boolean spaceFound = false, charFound = false;

        int result = 0;

        for(int i = s.length() - 1; i >= 0; i--)
        {

            if (s.charAt(i) == ' ' && charFound)
            {
                break;
            }
            if (s.charAt(i) == ' ' && !spaceFound)
            {
                spaceFound = true;
            }

            if (s.charAt(i) != ' ')
            {
                result ++;
                charFound = true;
            }
        }

        return result;
    }
}
