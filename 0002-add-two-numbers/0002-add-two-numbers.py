# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Placeholder to easily track the start of the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Continue loop if nodes remain or a carry needs to be added
        while l1 is not None or l2 is not None or carry != 0:
            # Get values, defaulting to 0 if list traversal is finished
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate sum and determine new carry
            total = val1 + val2 + carry
            carry = total // 10
            node_val = total % 10
            
            # Append new node and advance the current pointer
            current.next = ListNode(node_val)
            current = current.next
            
            # Move to the next nodes if available
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        return dummy_head.next
