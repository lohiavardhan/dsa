
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        return_node = new_head = ListNode()

        if n == 1 and head.next == None:
            return None

        new_head.next = head
        count = 0

        while count <= n - 1:
            new_head = new_head.next
            count += 1

        print(new_head.val)
        
        new_head.next = new_head.next.next if new_head.next else None

        return return_node.next