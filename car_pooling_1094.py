class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Since maximum number of location is 1000
        locations = [0] * 1001
        
        for trip in trips:
            locations[trip[1]] += trip[0]
            locations[trip[2]] -= trip[0]
            
        number_passengers = 0
        for i in range(len(locations)):
            number_passengers += locations[i]
            if number_passengers > capacity:
                return False
        
        return True
