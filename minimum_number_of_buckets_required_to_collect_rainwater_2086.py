class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        
        count = 0
        for i in range(len(street)):
            
            if street[i] == "H":
                if i - 1 >= 0  and street[i-1] == "B":
                    continue  
                
                if i + 1 < len(street) and  street[i+1] == ".":
                    street[i+1] = "B"
                    count += 1
                    
                elif i - 1 >= 0 and street[i-1] == ".":
                    street[i-1] = "B"
                    count += 1
                    
                else:
                    return -1
            
        return count
