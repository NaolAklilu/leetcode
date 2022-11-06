class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        temp = [0] * (n+1)
        for book in bookings:           
            temp[book[0]-1] += book[2]
            temp[book[1]] -= book[2]

        res = [0] * n
        sum = 0
        for i in range(len(temp)-1):
            sum += temp[i]
            res[i] = sum
        
        return res
        
