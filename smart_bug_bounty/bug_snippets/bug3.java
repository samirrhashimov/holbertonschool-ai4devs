public class PalindromeChecker {
    public static boolean isPalindrome(String str) {
        if (str == null) return false;
        
        String cleanStr = str.toLowerCase();
        int len = cleanStr.length();
        
        // Bug 1: Loop condition causes IndexOutOfBoundsException (i <= len)
        // Bug 2: Index character access logic logic flaw
        for (int i = 0; i <= len; i++) {
            if (cleanStr.charAt(i) != cleanStr.charAt(len - i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("racecar"));
    }
}