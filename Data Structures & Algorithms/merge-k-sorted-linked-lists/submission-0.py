# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNodeFoo:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # maintain a heap w len k
        head = ListNode(0)
        cur = head
        heap = []
        for i, l in enumerate(lists):
            heapq.heappush(heap, ListNodeFoo(l))

        while heap:
            # get the lowest value node
            node_wrapped = heapq.heappop(heap)
            cur.next = node_wrapped.node
            cur = cur.next

            if node_wrapped.node.next:
                heapq.heappush(heap, ListNodeFoo(node_wrapped.node.next))
        
        return head.next
