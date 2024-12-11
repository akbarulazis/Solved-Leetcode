class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        row = ['']*numRows
        current_row = 0
        direction = 1
        
        for char in s:
            row[current_row] += char
            if current_row ==0:
                direction = 1
            elif current_row >= numRows - 1:
                direction = -1
            current_row += direction
        
        return ''.join(row)