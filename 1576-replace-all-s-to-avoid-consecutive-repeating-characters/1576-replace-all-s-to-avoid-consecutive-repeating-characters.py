class Solution:
    def modifyString(self, s: str) -> str:
        abd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
              ,'o','p','q','r','s','t','u','v','w','x','y','z'
              ]
        k = list(s)
        if len(s) == 1 and s == '?':
            return 'a'
        for x in range(len(k)):
            if k[x] == '?' and x == 0:
                for i in range(len(abd)):
                    if abd[i] != k[x+1]:
                        k[x] = abd[i]
                        break
                    
            elif k[x] == '?' and x!=0:
                for i in range(len(abd)):
                    try:
                        if (abd[i] != k[x+1]) and (abd[i] != k[x-1]):
                            k[x] = abd[i]
                            break
                    except:
                        if  (abd[i] != k[x-1]):
                            k[x] = abd[i]
                            break
        return ''.join(k)
                    
        