class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        begin, end = 0, len(people) - 1
        count = 0
        
        people.sort()
        while begin <= end:
            if people[end] == limit:
                end -= 1
                count += 1
            elif people[begin] + people[end] <= limit:
                begin += 1
                end -= 1
                count += 1
            elif people[begin] + people[end] > limit:
                end -= 1
                count += 1
            
        return count        
