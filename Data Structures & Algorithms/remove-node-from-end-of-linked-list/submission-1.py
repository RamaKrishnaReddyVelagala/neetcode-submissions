# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # any removals kind of need dummy
        # remember dummy doesnt change until u make any changes to pointers. until then they only reference.

        # traverse with n distance between fast and slow.
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        
        counter = 0
        while counter<n:
            fast = fast.next
            counter = counter + 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next