# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':

        carry = 0

        head = None        
        output = None

        while (l1 or l2 or carry):
            
            l1Digit = 0
            l2Digit = 0
            sumOfDigits = 0

            if (l1):
                l1Digit = l1.val
            
            if (l2):
                l2Digit = l2.val

            sumOfDigits = l1Digit + l2Digit

            if (head):
                head.next = ListNode((sumOfDigits + carry) % 10)
            else:
                head = ListNode(sumOfDigits % 10)
                output = head

            if (sumOfDigits + carry >= 10):
                carry = 1
            else:
                carry = 0
            
            head = head.next if head.next else head
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return output

        

            

