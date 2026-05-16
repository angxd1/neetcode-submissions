class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}
        
        if len(s) != len(t):
            return False

        for i in s:
            if i in s_table:
                s_table[i] += 1
            else:
                s_table[i] = 1
        
        for i in t:
            if i in t_table:
                t_table[i] += 1
            else:
                t_table[i] = 1
        
        if t_table == s_table:
            return True

        return False
        
            

