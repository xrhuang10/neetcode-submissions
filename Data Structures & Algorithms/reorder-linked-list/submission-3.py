# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #divide list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        slow.next = None

        #reverse second list
        node = None
        while start:
            temp = start.next
            start.next = node
            node = start
            start = temp

        
        #merge two lists, one with head, one with node
        merged = ListNode()

        while node and head:
            merged.next = head
            head = head.next
            merged = merged.next

            merged.next = node
            node = node.next
            merged = merged.next
        
        merged.next = head or node
        
       

        


    
        
