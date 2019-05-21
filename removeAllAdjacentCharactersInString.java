class Solution {
    public String removeDuplicates(String S) {
        String s = S;
        if(s==null || s.length()<=1){
            return s;
        } 
         Stack<Character> stack  = new Stack();
          for(char c : s.toCharArray()){
              if( stack.size()>0 && stack.peek()==c){
                 stack.pop();
              }else{
                 stack.push(c);
              }
          }
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()) sb.append(stack.pop());
        return sb.reverse().toString();
    }
}
