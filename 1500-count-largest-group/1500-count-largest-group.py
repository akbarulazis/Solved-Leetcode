class Solution:
    def countLargestGroup(self, n: int) -> int:
        k = {}

        for x in range(1,n+1):
            if len(str(x)) == 1:
                if x not in k:
                    k[x] = [x]
            if len(str(x)) > 1:
                cnt = 0
                for i in str(x):
                    cnt = cnt + int(i)
                # cnt_2 = cnt
                # if cnt > 0:
                #     cnt = 0
                #     for i in str(cnt_2):
                #         cnt = cnt + int(i)
                
                if cnt in k:
                    k[cnt] = k[cnt] + [x]
                else:
                    k[cnt] = [x]

        all_len = [len(y) for x,y in k.items()]
        max_len = max(all_len)
        res = 0 

        for x in all_len:
            if x == max_len:
                res += 1
                
        return res

