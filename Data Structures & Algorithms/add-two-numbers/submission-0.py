# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1, cur2 = l1, l2
        s1, s2 = str(), str()

        while cur1:
            s1 = s1 + str(cur1.val)
            cur1 = cur1.next
        while cur2:
            s2 = s2 + str(cur2.val)
            cur2 = cur2.next
        s1, s2 = s1[::-1], s2[::-1]
        answer = str(int(s1) + int(s2))[::-1]
        print(answer)

        dummy = ListNode(-1)
        curr = dummy
        
        for i in range(len(answer)):
            curr.next = ListNode(int(answer[i]))
            curr = curr.next
        return dummy.next