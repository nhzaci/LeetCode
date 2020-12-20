# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # naive solution
        # faster than 93.08% of submissions
        full_list = []
        final = ListNode('')
        final_ptr = final
        for (idx, lList) in enumerate(lists):
            while lList:
                full_list.append(lList.val)
                lList = lList.next

        full_list.sort()
        for (idx, item) in enumerate(full_list):
            final.val = item
            if idx != len(full_list) - 1:
                final.next = ListNode()
                final = final.next

        return final_ptr
