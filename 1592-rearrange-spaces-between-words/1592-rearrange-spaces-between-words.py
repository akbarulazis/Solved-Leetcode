class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(' ')
        
        if len(words) == 1:
            return words[0] + (spaces*' ')
        
        spc_bet = spaces // (len(words)-1)
        spc_left = spaces % (len(words)-1)
        
        res = (' '*spc_bet).join(words)
        
        return res + (spc_left*' ')