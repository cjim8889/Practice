# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        l = head
        
        
        resultHead = None
        resultTail = None
        
        tempHead = None
        temp = None
        f = False
        while l != None:
            if (l.val < x and resultHead == None):
                resultHead = l
                resultTail = resultHead
                l = l.next
                continue
            
            if (l.val < x):
                if (f):
                    resultTail.next = l
                    f = False
                l = l.next
                resultTail = resultTail.next
                continue
            else:
                f = True
                if (tempHead == None):
                    tempHead = l
                    l = l.next
                    tempHead.next = None
                    temp = tempHead
                else:
                    temp.next = l
                    l = l.next
                    temp = temp.next
                    temp.next = None
        
        
        
        if (tempHead):
            if (resultTail):
                resultTail.next = tempHead
                return resultHead
            else:
                return tempHead
        
        return resultHead
        