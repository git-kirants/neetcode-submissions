# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # finding the half of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing the second half of the list
        second = slow.next # slow.next points to the start of the second half of org
        slow.next = None # init for reverse
        prev = None # init for reverse
        
        while second:
            temp = second.next 
            second.next = prev
            prev = second
            second = temp

        # after reversing prev would be standing on the last element which would be the new head
        # merging the two list

        first , second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2