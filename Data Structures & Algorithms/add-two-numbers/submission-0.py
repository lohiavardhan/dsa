# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = l1

        number_1 = ""
        while head:
            number_1 += str(head.val)
            head = head.next

        head = l2
        number_2 = ""
        while head:
            number_2 += str(head.val)
            head = head.next
        
        answer_int = int(number_1[::-1]) + int(number_2[::-1])

        returnval = new_ll = ListNode()

        while answer_int > 10:
            new_ll.val = answer_int % 10
            answer_int = answer_int // 10
            new_ll.next = ListNode()
            new_ll = new_ll.next
        
        new_ll.val = answer_int
        new_ll.next = None

        return returnval