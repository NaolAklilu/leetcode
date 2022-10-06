# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next          
        
        if n == count:
            del_node = head
            head = head.next
            del del_node
            return head
                
        nth = count - n + 1
        i = 1
        
        nextNode = head
        while i < nth-1:
            nextNode = nextNode.next
            i += 1
                    
        del_node = nextNode.next
        nextNode.next = del_node.next
        del del_node       
            
        return head
