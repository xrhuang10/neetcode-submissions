# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None

        if n == 1:
            answer = head
            while head.next:
                before = head
                head = head.next
            before.next = None
            return answer
            
        #reverse the linked list
        prev = None
        
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        #now prev points to head of reversed list
        skipper = reversedhead = prev
        
        #remove nth node
        for i in range(n - 2):
            skipper = skipper.next #now points to node we want to remove

        temp = skipper.next.next
        skipper.next = temp
        
        
        #reverse it back
        reversedprev = None
        while reversedhead:
            temp = reversedhead.next
            reversedhead.next = reversedprev
            reversedprev = reversedhead
            reversedhead = temp
        
        return reversedprev
