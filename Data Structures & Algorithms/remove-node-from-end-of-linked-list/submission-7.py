# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head

        #reverse
        reversedhead = None
        while head:
            temp = head.next
            head.next = reversedhead
            reversedhead = head
            head = temp

        #remove nth
        remover = reversedhead
        if n == 1:
            temp = reversedhead.next
            reversedhead = temp
            
        else:
            for i in range(n - 2):
                remover = remover.next
            if remover.next:
                remover.next = remover.next.next
            else:
                return None
            

        #reverse back
        prev = None
        while reversedhead:
            temp = reversedhead.next
            reversedhead.next = prev
            prev = reversedhead
            reversedhead = temp
        
        return prev
        
        
