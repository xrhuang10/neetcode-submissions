# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        initial, fast, slow = head, head, head
        while fast and fast.next: #finds middle point
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second: #reverses second list
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        answer = builder = ListNode()
        while prev and initial:
            builder.next = initial
            initial = initial.next
            builder = builder.next

            builder.next = prev
            prev = prev.next
            builder = builder.next
        
        builder.next = prev or initial
    
        
