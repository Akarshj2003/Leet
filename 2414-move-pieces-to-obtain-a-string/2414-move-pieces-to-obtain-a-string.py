class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start==target:
            return True
        s_positions = [(ch, i) for i, ch in enumerate(start) if ch != '_']
        t_positions = [(ch, i) for i, ch in enumerate(target) if ch != '_']
        
    
        if len(s_positions) != len(t_positions):
            return False
        
        for (s_ch, s_idx), (t_ch, t_idx) in zip(s_positions, t_positions):
           
            if s_ch != t_ch:
                return False
            if s_ch == 'L' and s_idx < t_idx:
                return False  
            if s_ch == 'R' and s_idx > t_idx:
                return False  
        
        return True
