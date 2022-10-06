# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if head == None:
            return head
        
        nextNode = temp.next
        while nextNode != None and temp != None:
            if temp.val == nextNode.val:
                temp.next = nextNode.next
            else:
                temp = nextNode
            nextNode = nextNode.next
            
        return head
