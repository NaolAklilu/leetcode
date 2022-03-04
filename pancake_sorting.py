def flip(arr, max_num):
        start = 0
        while(start < max_num):
            temp = arr[start]
            arr[start] = arr[max_num]
            arr[max_num] = temp
            start += 1
            max_num -= 1
        return arr

def find_max(arr, m):
    max_num_index = 0
    for i in range(m):
        if(arr[i] > arr[max_num_index]):
            max_num_index = i

    return max_num_index

class Solution:
    def pancakeSort(self,arr: List[int]) -> List[int]:
        current_size = len(arr)
        flip_index = []
        while current_size > 1:
            max_index = find_max(arr, current_size)        
            if max_index != current_size - 1:
                flip_index += str(max_index + 1)

                flip(arr, max_index)
                flip(arr, current_size - 1)
            current_size -= 1

        return flip_index
