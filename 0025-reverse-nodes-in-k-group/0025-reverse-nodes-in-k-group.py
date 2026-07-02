class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        while True:
            ktail = group_prev
            for _ in range(k):
                ktail = ktail.next
                if not ktail:
                    break
            if not ktail:
                break
            prev = ktail.next
            curr = group_prev.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = group_prev.next
            group_prev.next = prev
            group_prev = temp
        return dummy.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna