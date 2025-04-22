class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        k = {}
        res = []
        for x,y in enumerate(groupSizes):
            if y not in k:
            
                k[y] = [x]
            else:
                z =  k[y].append(x)

        for x,y in k.items():
            print(x,y)
            cnt = []
            for z in y:
                print(z)
                cnt.append(z)
                if len(cnt) == x:
                    res.append(cnt)
                    cnt = []
        return res