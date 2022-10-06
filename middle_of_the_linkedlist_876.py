# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        
        if head == None:
            return head
        
        while temp != None:
            count += 1
            temp = temp.next
        
        mid = (count // 2) + 1
        
        i=1
        while i < mid:
            head = head.next
            i += 1
        
        return head
