class Solution:
    def maxOperations(self, arr: List[int], k: int) -> int:
        arr.sort()

        low = 0
        high = len(arr) - 1

        answer = 0
        while(low < high):
            if ((arr[low] + arr[high]) == k):
                low += 1
                high -= 1
                answer += 1

            elif(arr[low] + arr[high] < k ):
                low += 1

            else:
                high -= 1
        return(answer)
