

class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> d_s = new HashMap<>();
        Map<Character, Integer> d_t = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            d_s.put(
                s.charAt(i),
                1 + d_s.getOrDefault(s.charAt(i), 0)
            );

            d_t.put(
                t.charAt(i),
                1 + d_t.getOrDefault(t.charAt(i), 0)
            );
        }

        for (Character l : d_s.keySet()) {
            if (!d_s.get(l).equals(d_t.getOrDefault(l, -1))) {
                return false;
            }
        }

        return true;
    }
}