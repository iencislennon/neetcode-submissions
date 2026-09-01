class Solution {
    public boolean validPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;
        while (l<r){
            if (s.charAt(l) != s.charAt(r)){
                String skipl = s.substring(l+1,r+1);
                String skipr = s.substring(l, r);
                String reverse_skipl = new StringBuilder(skipl).reverse().toString();
            String reverse_skipr = new StringBuilder(skipr).reverse().toString();
            if (skipl.equals(reverse_skipl) || skipr.equals(reverse_skipr)) {return true;} return false;
            
            }
            l ++; 
            r--;
            
        }
        

    return true; 
    } 
}