class Solution:
    def insertion_sort(self, arr):
        max = arr[0][0]
        for i in arr:
            if i[0] > max:
                max = i[0]

        count_arr = [[] for _ in range(0,max+1)]

        for i in arr:
            count_arr[i[0]].append(i)

        sorted_arr = []
        for arr in count_arr:
            for i in arr:
                sorted_arr.append(i)

        return sorted_arr
    
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        coordinates = []
        sorted_coordinates = []
        
        for row in range(0, rows):
            for col in range(0, cols):
                coordinates.append([row, col])
        
        distance_array = []
        for coordinate in coordinates:
            distance = abs(coordinate[0] - rCenter) + abs(coordinate[1] - cCenter)
            distance_array.append((distance, coordinate))
            
        sorted_distance = self.insertion_sort(distance_array)
        for coord in sorted_distance:
            sorted_coordinates.append(coord[1])
            
        return sorted_coordinates
