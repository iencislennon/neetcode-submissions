class Solution {
    public void reverseString(char[] s) {
        int r = s.length - 1;
        for(int l=0; l<s.length/2; l++){
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            r--;
        }
    }
}