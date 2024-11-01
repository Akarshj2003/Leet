class Solution:
    def makeFancyString(self, s: str) -> str:
        stack=[]
        c=0
        for i in s:
            if not stack or (stack[-1]==i and c==0) or stack [-1] != i:
                if not stack:
                    stack.append(i)
                elif  stack[-1]==i:
                    c+=1
                    stack.append(i)
                else:
                    c=0
                    stack.append(i)

                    
        st="".join(stack)
               
        return st
                
        