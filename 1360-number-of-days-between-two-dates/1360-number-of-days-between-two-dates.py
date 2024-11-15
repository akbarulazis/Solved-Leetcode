from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = date1.split('-')
        d2 = date2.split('-')
        
        dd1 = date(int(d1[0]),int(d1[1]),int(d1[2]))
        dd2 = date(int(d2[0]),int(d2[1]),int(d2[2]))
        
        return abs(dd1-dd2).days
        