class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=""
        de=1
        for i in s:
            if i in st:
                st=""
                de+=1
            st += i     
        return de