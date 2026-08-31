class Solution {
    public int removeElement(int[] nums, int val) {
        int k =0;
        int r = 0; 
        for (int l=0; l<nums.length; l++){
            if (val != nums[l]){
                int temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
                k++;
                r++;
                
            }

        }
        return k; 
    }
}