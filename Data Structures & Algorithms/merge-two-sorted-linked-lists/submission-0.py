# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1

        head1 = list1
        p1, p2 = list1, list2

        while p1.next is not None and p2.next is not None:
            if p1.next.val < p2.val:
                p1 = p1.next
            else:
                temp = p1.next
                p1.next = p2
                temp2 = p2.next
                p1.next.next = temp
                p2 = temp2
                p1 = p1.next

        if p1.next is not None:
            while p1.next:
                p1 = p1.next
        
        p1.next = p2


        return head1 
