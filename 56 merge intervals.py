class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda interval:interval[0])
        stack_list = []
        
        stack_list.append(intervals[0])
        
        for interval in intervals[1:]:
            if stack_list[-1][0] <= interval[0] and  interval[0] <= stack_list[-1][1]:
                if stack_list[-1][1] > interval[1]:
                    stack_list[-1][1] = stack_list[-1][1]
                elif stack_list[-1][1] < interval[1]:
                    stack_list[-1][1] = interval[1]
                else:
                    stack_list[-1][1] = interval[1]
            else:
                stack_list.append(interval)
        return stack_list
