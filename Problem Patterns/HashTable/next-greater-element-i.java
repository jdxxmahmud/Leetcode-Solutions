// Problem Link: https://leetcode.com/problems/next-greater-element-i

class Solution {

    Map<Integer, Integer> hashTab= new HashMap<>();

    public void findElementPosition(int[] arr)
    {
        for(int i = 0; i < arr.length; i++)
        {
            this.hashTab.put(arr[i], i);
        }
    }

    public int[] nextGreaterElement(int[] nums1, int[] nums2) {

        this.findElementPosition(nums2);

        int[] res = new int[nums1.length];
        Arrays.fill(res, -1);
        int currPos = 0;
        
        for(int num: nums1)
        {
            int startingRange = this.hashTab.get(num);

            for(int i = startingRange; i < nums2.length; i++)
            {
                if(nums2[i] > num)
                {
                    res[currPos] = nums2[i];
                    break;
                }
            }
            currPos++;
        }

        return res;
    }
}
