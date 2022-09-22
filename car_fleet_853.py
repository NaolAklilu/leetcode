class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        position_speed_pair = []
        time_taken = []
            
        position_speed_pair = sorted(zip(position, speed), reverse=True)
        
        for i in range(len(position)):
            time_taken.append((target - position_speed_pair[i][0]) / position_speed_pair[i][1])
        
        for time in time_taken:
            if len(stack) == 0:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
                
        return len(stack)
