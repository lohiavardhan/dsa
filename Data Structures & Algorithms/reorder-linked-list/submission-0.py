# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        top = head

        count = 0
        while top:
            top = top.next
            count += 1
        
        mid = count // 2

        mid_node = head
        count = 0
        while count < mid:
            mid_node = mid_node.next
            count += 1
        
        
        prev, curr = None, mid_node

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        old = head

        count = 1
        new = ListNode()

        while prev and old:
            print(new.val)
            if count % 2 == 0:
                new.next = prev
                prev = prev.next
            else:
                new.next = old
                old = old.next
            
            new = new.next
            count += 1
        
        head = new.next

