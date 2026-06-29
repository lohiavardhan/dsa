# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = answer_list = ListNode()
        
        while True:
            curr_min = ListNode(float("infinity"))
            if all(not lists[i] for i in range(len(lists))):
                return dummy.next
            
            for i in range(len(lists)):
                if lists[i] and lists[i].val < curr_min.val:
                    index = i
                    curr_min = lists[i]
            
            
            answer_list.next = curr_min
            answer_list = answer_list.next
            lists[index] = lists[index].next

