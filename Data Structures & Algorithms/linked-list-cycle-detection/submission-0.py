# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        counts = 0
        while curr.next and counts < 1000:
            counts += 1
            curr = curr.next 

        if curr.next:
            return True
        return False