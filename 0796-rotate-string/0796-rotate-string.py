class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        goal2 = goal+goal
        if len(goal) < len(s):
            return False
        return s in goal2