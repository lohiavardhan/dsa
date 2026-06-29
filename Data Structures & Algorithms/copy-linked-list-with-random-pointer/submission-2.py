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
        
        if not head:
            return None

        top2 = top = head

        nodes = {}
        while top:
            nodes[top] = Node(top.val)
            top = top.next
        
        
        while top2:
            nodes[top2].next = nodes[top2.next] if top2.next else None 
            nodes[top2].random = nodes[top2.random] if top2.random else None
            top2 = top2.next

        return nodes[head]
