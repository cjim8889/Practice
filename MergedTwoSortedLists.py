# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':

        if (not l1):
            return l2
        
        if (not l2):
            return l1


        output = None
        head = None


        if (l1.val <= l2.val):
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        output = head

        while (l1 and l2):

                                                
            if (l1.val <= l2.val):

                head.next = l1
                l1 = l1.next
            
            else:

                head.next = l2
                l2 = l2.next

            head = head.next

        remains = l1 if l1 else l2

        head.next = remains
        


        return output
                