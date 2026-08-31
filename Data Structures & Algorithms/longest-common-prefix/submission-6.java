class Solution {
    public String longestCommonPrefix(String[] strs) {
        int min = 201;
        for (int s = 0; s<strs.length; s++){
            if (strs[s].length() < min){
                min = strs[s].length();
            }
        }

        int i = 0;
        while (i < min){
            for (int s=0; s < strs.length; s++){
                String str = strs[s];
                String checker = strs[0];
                if (str.charAt(i) != (checker.charAt(i))){
                    return strs[0].substring(0, i);
                }
            }
            i++;
        }
        return strs[0].substring(0, i);
    }
}