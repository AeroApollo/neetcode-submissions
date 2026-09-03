# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # while loop w a counter. 
        # counter = n 
            
            # reconnect prev.next = self.next.

            # disconnect self.next = None
        # but what if n = 0
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr=curr.next
        #print(counter)
        rm_target = counter-n
        curr = head
        prev = None
        counter = 0
        while curr:
            if counter == rm_target:
                if curr == head:
                    head = curr.next
                    return head
                prev.next = curr.next
                return head
            prev = curr
            curr = curr.next
            counter += 1
