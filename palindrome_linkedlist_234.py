# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
            
        for i in range(len(res) // 2):
            if res[i] != res[len(res) - 1 - i]:
                return False
            
        return True
            
