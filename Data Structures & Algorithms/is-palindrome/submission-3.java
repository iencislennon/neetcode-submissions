class Solution {
    public boolean isPalindrome(String s) {
        String alp = "qwertyuiopasdfghjklzxcvbnm1234567890";
        s = s.toLowerCase();
        String clean_s = "";
        for (int i=0; i < s.length(); i++){
            if (alp.contains(String.valueOf(s.charAt(i)))){
                clean_s += s.charAt(i); 
            }
        }
        int r = clean_s.length()-1;
        for (int l=0; l<clean_s.length(); l++){
            if (clean_s.charAt(l) != clean_s.charAt(r)){
                return false;
            }
            r--;
        }
        return true; 
    }
}
