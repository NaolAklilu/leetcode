class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        answer = []
        for point in points:
            dist = [math.sqrt(point[0] ** 2 + point[1] ** 2), point]
            distance.append(dist)
        new_array = sorted(distance)
        for i in range(0,k):
            answer.append(new_array[i][1])
        return(answer)
