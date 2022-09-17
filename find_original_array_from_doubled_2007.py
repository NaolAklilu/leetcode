class Solution(object):
    def findOriginalArray(self, changed):
        changed.sort()
        size = len(changed)
        
        list_one = []
        result_list = []
        
        if size % 2 != 0:
            return []

        for num in changed:
            if len(list_one) > 0 and num == 2*list_one[0]:
                result_list.append(list_one.pop(0))
            else:
                list_one.append(num)

        if len(list_one) != 0:
            return []
        else:
            return result_list
