import java.util.Stack;

class Solution {
    public boolean isValid(String s) {

        Stack<Character> stack = new Stack<>();

        for(Character character : s.toCharArray()) {

            if(character == ' ') continue;

            else if(character == '(' || character == '{' || character == '[') {
                stack.push(character);
            }
            else if(stack.isEmpty()) return false;
            else if(character == ')' && stack.pop() != '(' ) return false;
            else if(character == '}' && stack.pop() != '{' ) return false;
            else if(character == ']' && stack.pop() != '[' ) return false;

        }


        return stack.isEmpty();
    }
}