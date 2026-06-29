"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        top2 = top = head
        
        remove_last = return_node = random_add = new_head = Node(head.val)

        added = {}
        while top:
            new_head.val = top.val
            added[new_head.val] = new_head
            new_head.next = Node(top.next.val) if top.next else None
            new_head = new_head.next
            top = top.next
        
        while random_add and top2:
            if top2.random:
                random_add.random = added[top2.random.val]
            else:
                random_add.random = None
            random_add = random_add.next
            top2 = top2.next

        return return_node
