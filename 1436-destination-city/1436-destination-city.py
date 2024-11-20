class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        first_city = [x[0] for x in paths]
        second_path = [x[1] for x in paths]
        
        for x in second_path:
            if x not in first_city:
                return x