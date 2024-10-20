class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l= []
        l2 = []
        res = []
        for x in range(len(list1)):
            for y in range(len(list2)):
                if list1[x] == list2[y]:
                    l.append(x)
                    l2.append(x+y)
        for x in range(len(l2)):
            if l2[x] == min(l2):
                res.append(list1[l[x]])
        
        return res