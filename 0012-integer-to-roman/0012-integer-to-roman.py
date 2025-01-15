class Solution:
    def intToRoman(self, num: int) -> str:
        map_roman = [
    (1000,'M'), (900,'CM'), (500,'D'), (400,'CD')
   , (100,'C'), (90,'XC'), (50,'L'), (40,'XL')
   , (10,'X'), (9,'IX'),(5,'V'), (4,'IV'),(1,'I') 
    
        ]   

        res = []
        for number, symbol in map_roman:
            if num == 0:
                break
        
        
            count, num = divmod(num,number)
            if count > 0:
                res.append(count*symbol)
    
        return ''.join(res)
            