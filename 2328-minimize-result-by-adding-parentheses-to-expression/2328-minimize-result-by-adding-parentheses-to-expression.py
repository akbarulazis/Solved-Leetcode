class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split('+')
        max_value = float('inf')

        for i in range(len(num1)):
            for j in range(1,len(num2)+1):
                left_part =int( num1[:i]) if i > 0 else 1

                right_part =int( num2[j:] ) if j < len(num2) else 1
        
                middle_part = int(num1[i:]) +int(num2[:j])
            
                
                result = left_part * middle_part * right_part
                
                if result < max_value:
                    max_value = result
                    best = (
                        ( num1[:i] + '(' if i > 0 else '(' )
                        + num1[i:] + '+'+ num2[:j] +
                         ( ')' + num2[j:]   if j < len(num2) else ')')
                        )
        return best