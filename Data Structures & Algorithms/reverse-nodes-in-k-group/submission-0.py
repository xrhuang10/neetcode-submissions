# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        

        while True:

            kth = self.getkth(groupPrev, k) #will mark the end of the list to reverse
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
                    # step 3: reconnect
            tmp = groupPrev.next      # old head of group (now tail)
            groupPrev.next = kth      # connect previous group to new head
            groupPrev = tmp           # move groupPrev to tail of reversed group

        return dummy.next


    def getkth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
            
        


