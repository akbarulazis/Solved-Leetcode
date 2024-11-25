class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":'01', "Feb":'02'
         , "Mar":'03', "Apr":'04', "May":'05', "Jun":'06'
         , "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        
        k = date.split(' ')
        res = []
        for x in range(len(k)):
            if x == 0:
                if len(k[x]) == 4:
                    res.append(k[x][:2])
                else:
                    f = '0'+k[x][:1]
                    res.append(f)
            elif x == 1:
                res.append(month[k[x]])
            else:
                res.append(k[x])
        
        res.reverse()
        
        return '-'.join(res)