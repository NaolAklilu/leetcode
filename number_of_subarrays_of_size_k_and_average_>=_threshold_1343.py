class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, right = 0, 0
        total = 0
        count = 0
        
        while right <= len(arr) - 1:
            while (right - left + 1) <= k:
                total += arr[right]
                right += 1
            
            if (total / k) >= threshold:
                count += 1
                
            total -= arr[left]
            left += 1
        
        return count
