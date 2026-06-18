class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums); // Sort the array to bring duplicates together
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return true; // Return true if a duplicate is found
            }
        }
        return false; // Return false if no duplicates are found after the loop
    }
}
