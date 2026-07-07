# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Input: list1 = [1,2,4], list2 = [1,3,5]
        # Output: [1,1,2,3,4,5]

        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif not list1 and not list2:
            return list1

        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        
        curr = head

        while list1 and list2: 
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list1:
            while list1:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
        else:
            while list2:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        
        return head


