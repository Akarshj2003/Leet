class Solution {
    public int partitionString(String s) {
        int de = 1;
        String su = "";
        for(char i : s.toCharArray()){
            if(su.indexOf(i) != -1){
                de++;
                su = "";
            }
            su += i;
        }
        return de;
        
    }
}