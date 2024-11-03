class Solution {
    public int partitionString(String s) {
        boolean[] HashSet= new boolean[26];
        int count=1;
        for(int i=0;i<s.length();i++)
        {
            if(HashSet[s.charAt(i)-'a'])
            {
                count+=1;
                HashSet=new boolean[26];
            }
            HashSet[s.charAt(i)-'a']=true;
        }
        return count;
    }
}