# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        test = head
        count = 0
        while test:
            test = test.next
            count += 1
        
        to_remove = count - n 

        i = 0
        new_list = ListNode()
        new_list.next = head
        node_before = new_list
        while i <= to_remove - 1:
            node_before = node_before.next
            i += 1
        
        print(node_before.val)

        node_before.next = node_before.next.next if node_before.next else None

        return new_list.next