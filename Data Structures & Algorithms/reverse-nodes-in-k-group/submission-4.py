# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getkth(self, node, k):
            while k > 0 and node:
                node = node.next
                k -= 1
            return node
        
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = getkth(self, groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            curr, prev = groupPrev.next, kth.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        

        return dummy.next
        
        
        

