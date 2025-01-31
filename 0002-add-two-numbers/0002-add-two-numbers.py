# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        while l1 is not None:
            li.append(l1.val)
            l1   = l1.next
        li.reverse()
        lii = []
        while l2 is not None:
            lii.append(l2.val)
            l2 = l2.next
        lii.reverse()

        k1 = int(''.join(str(x) for x in li))
        k2 = int(''.join(str(x) for x in lii))

        k3 = k1+k2


        l3 = [int(x) for x in str(k3)]
        l3.reverse()

        curr = ListNode(l3[0])
        head = curr

        for i in l3[1:]:
            temp = ListNode(i)
            curr.next = temp
            curr = temp

        return head
        