# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:     
        res = ListNode()
        cur_sum = res
        
        rem = 0
        
        while l1 or l2:
            if l1 and l2 == None:
                sum = l1.val + rem
                l1 = l1.next
            elif l2 and l1 == None:
                sum = l2.val + rem
                l2 = l2.next
            elif l1 and l2:  
                sum = l1.val + l2.val + rem
                l1 = l1.next
                l2 = l2.next
                
            cur_sum.next = ListNode(sum%10)
            cur_sum = cur_sum.next   
            rem = sum//10
            
        if rem > 0:
            cur_sum.next = ListNode(rem)
            cur_sum = cur_sum.next
            
        return res.next
   
