# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if lists == []:
            return None
        def mergeTwoLists(listA, listB):
            head1 = listA
            head2 = listB
            dummy = curr = ListNode()
            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next

            curr.next = head1 or head2

            return dummy.next

        answer = lists[0]
        for i in range(1, len(lists)):
            listToMerge = lists[i]
            answer = mergeTwoLists(answer, listToMerge)
        
        return answer
