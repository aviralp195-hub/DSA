# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):

        slow = head
        fast = head

        # Step 1: Detect if cycle exists
        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        # No cycle found
        if fast is None or fast.next is None:
            return None

        # Step 2: Find the starting node of the cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
        
        