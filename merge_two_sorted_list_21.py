# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        list1head = list1
        list2head = list2
        
        res = ListNode()
        temp = res
        
        while list1head != None and list2head != None:
            if list1head.val <= list2head.val:
                temp.next = list1head
                list1head = list1head.next
            else:
                temp.next = list2head
                list2head = list2head.next
                
            temp = temp.next

        
        if list1head != None:
            temp.next = list1head
                
        elif list2head != None:
            temp.next = list2head
            
        return res.next
            
