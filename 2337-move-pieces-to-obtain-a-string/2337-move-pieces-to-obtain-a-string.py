class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        
        l_need = 0
        r_avail = 0
        
        for s, t in zip(start, target):
            if s == 'R':
                if l_need > 0:
                    return False
                r_avail += 1
            
            if t == 'L':
                if r_avail > 0:
                    return False
                l_need += 1
            
            if t == 'R':
                if r_avail == 0:
                    return False
                r_avail -= 1
            
            if s == 'L':
                if l_need == 0:
                    return False
                l_need -= 1
        
        return l_need == 0 and r_avail == 0

