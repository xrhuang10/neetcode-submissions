# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        
        def mergeTwoLists(list1, list2):
            head = builder = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    builder.next = list1
                    list1 = list1.next
                else:
                    builder.next = list2
                    list2 = list2.next
                
                builder = builder.next
            
            builder.next = list1 or list2
            return head.next
        
        merged = None
        for item in lists:
            merged = mergeTwoLists(item, merged)
        
        return merged
        
