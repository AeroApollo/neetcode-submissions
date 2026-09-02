# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # combination of merging two lists and reversing and cycles
        # sub problem 1: return ascenduing order
        # sub problem 2: find and return the end of linkedlist (reverse after asending
        # sub problem 3: terminate while when the subprob 1 or 2 has seen a prev input node

        #first pass 
        # run through linkedlist to get total length
        # create a new linkedlist that is reversed
        # you could then combine the by combine both lists with terminating condition of a seen = set()

        # reversin a linkedlist

        # split the linked list into halves
        slow, fast = head, head.next # set slow =
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split by setting slow.next = None
        second = slow.next
        slow.next = None
        # reverse the linkedlist of second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge
        # second half is shorter
        first, second = head, prev
        while second:
            tmp = first.next #store old link
            first.next = second
            tmp2 = second.next
            second.next = tmp
            first = tmp
            second = tmp2