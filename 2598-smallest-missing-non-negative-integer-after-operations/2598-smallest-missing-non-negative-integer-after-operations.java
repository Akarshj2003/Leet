class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        Map<Integer,Integer> mp = new HashMap<>();
        for(int num:nums){
            int r=((num%value)+value)%value;
            mp.put( r , mp.getOrDefault(r , 0) + 1);
        }
        int mex=0;
        while(mp.getOrDefault(mex % value , 0) > 0){
            mp.put(mex % value , mp.get(mex % value)-1);
            mex++;
        }
        return mex;
    }
}