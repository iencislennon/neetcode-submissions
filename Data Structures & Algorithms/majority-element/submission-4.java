class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> d = new HashMap<>();
        int n = nums.length;
        for (int i=0; i<nums.length; i++){
            d.put(nums[i], 1 + d.getOrDefault(nums[i] ,0));
        }
        for (int i=0; i<nums.length; i++){
            if (d.get(nums[i]) > n/2){

                return nums[i];
            }
        }
        return nums[0];
    }
}