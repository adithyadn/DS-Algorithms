public class Solution {


    public String longestPalindrome(String s) {


        int maxPallinLength = 0;
        int startIndex = 0; int endIndex = 0;
        if(s == null || s.length() == 0) return "";
        for(int index = 0; index < s.length(); index++) {
            int lengthLeft = pallindromeLengthFromCenter(s, index, index);
            int lengthRight = pallindromeLengthFromCenter(s, index, index + 1);
            int maxLength = Math.max(lengthLeft, lengthRight);

            if(maxPallinLength < maxLength) {
                maxPallinLength = maxLength;
                startIndex = index - (maxPallinLength -1) / 2;
                endIndex = index + maxPallinLength / 2;
            }
        }

        return s.substring(startIndex, endIndex+1);
    }

    public int pallindromeLengthFromCenter(String str, int left, int right) {
        int length = 0;
        while(left >= 0 && right < str.length() && str.charAt(left) == str.charAt(right)) {
            left --;
            right++;
            length++;
        }

        return right - left - 1;
    }

    public String longestPalindromeBruteForce(String s) {

        for(int length = s.length(); length >= 1; length--) {
            for(int index = 0; index <= s.length() - length; index++) {
                if(checkIfPallindrome(s.substring(index, index + length)))
                    return s.substring(index, index+length);
            }
        }

        return "";

    }

    public boolean checkIfPallindrome(String str) {
        for(int index = 0; index < str.length() / 2; index++) {
            if(str.charAt(index) != str.charAt(str.length() - index - 1))
                return false;
        }

        return true;
    }
}