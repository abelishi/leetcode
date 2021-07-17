class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if len(p) == 0:
            return len(s) == 0
        
        if len(p) == 1 and p == '.':
            return len(s) == 1
        
        if len(p) == 1 and p.isalpha():
            return s == p
        
        if p[:2] == '.*':
            for i in range(len(s) + 1):
                if self.isMatch(s[i:], p[2:]):
                    return True
        elif p[1] == '*':
            if self.isMatch(s, p[2:]):
                return True
            
            for i in range(len(s)):
                if s[i] != p[0]:
                    break
                if self.isMatch(s[i+1:], p[2:]):
                    return True           
        elif len(s) and (p[0] == '.' or p[0] == s[0]):
            return self.isMatch(s[1:], p[1:])
        
        return False
