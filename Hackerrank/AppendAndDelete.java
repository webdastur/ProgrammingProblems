package Hackerrank;

class AppendAndDelete {
    public static void main(String[] args) {
        System.out.println(appendAndDelete("abc", "def", 6));
        System.out.println(appendAndDelete("aba", "aba", 7));
        System.out.println(appendAndDelete("ashley", "ash", 2));
        System.out.println(appendAndDelete("y", "yu", 2));
    }

    public static String appendAndDelete(String s, String t, int k) {
        int count = 0;
        while (count < Math.min(s.length(), t.length())) {
            if (s.charAt(count) != t.charAt(count)) break;
            count++;
        }
        int sLeftLength = s.length() - count;
        int tLeftLength = t.length() - count;

        if (sLeftLength + tLeftLength <= k && ((k - sLeftLength + tLeftLength) % 2 == 0 || (k - tLeftLength + sLeftLength) > 2 * count)) {
            return "Yes";
        }
        return "No";
    }
}