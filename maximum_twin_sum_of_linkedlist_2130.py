# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        val_list = []
        cur = head
        
        res = []
        
        while cur:
            val_list.append(cur.val)
            cur = cur.next
            
        n = len(val_list)
        for i in range(n//2):
            res.append(val_list[i] + val_list[n-1-i])
        
        return max(res)
