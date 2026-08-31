class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> d = new HashMap<>();
        for (int i=0; i<nums.length; i++){
            int val = nums[i];
            int diff = target - nums[i];
            if (d.containsKey(diff)){
                return new int[]{d.get(diff), i};
            }
            d.put(val, i);

        }
        return new int[]{};
    }
}
