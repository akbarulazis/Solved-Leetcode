class Solution:
    def dayOfYear(self, date: str) -> int:
        nokab = [31,28,31,30,31,30,31,31,30,31,30,31]
        kab = [31,29,31,30,31,30,31,31,30,31,30,31]
        
        l = date.split('-')
        tahun = int(l[0])
        if ( ( (tahun%4==0) and (tahun%100 != 0)) or (tahun%400==0) ):
            k = sum(kab[:int(l[1])-1]) + int(l[2])
            return k
        else:
            k = sum(nokab[:int(l[1])-1]) + int(l[2])
            return k