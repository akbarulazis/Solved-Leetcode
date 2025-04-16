class Solution:
    def reverseDegree(self, s: str) -> int:
        st = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

        k = st.split(' ')
        k.reverse()




        count = 0
        for i in range(len(s)):

            count += ( k.index(s[i]) + 1 ) * ( i + 1 ) 

            
        return count