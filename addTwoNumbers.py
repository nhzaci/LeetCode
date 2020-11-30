# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Create list of nodes with a sum and a carry
        For each sum, add the carry in and check if its greater than 10
        If greater than 10, carry over to the next carry
        Lastly if the loop has ended and carry != 0, add it to last node
        Time Complexity: O(n)
        '''
        # create the first list nodes with values
        first_sum = (l1.val + l2.val) % 10
        # initialise the first carry value
        carry = (l1.val + l2.val) // 10
        final_node = ListNode(first_sum)
        first_node_pointer = final_node
        i = 0
        # for subsequent ones, while not last, continue initialising the values
        while not l1.next is None or not l2.next is None:
            next_l1_val = l1.next.val if not l1.next is None else 0
            next_l2_val = l2.next.val if not l2.next is None else 0
            final_node.next = ListNode(
                (next_l1_val + next_l2_val + carry) % 10)
            carry = (next_l1_val + next_l2_val + carry) // 10
            l1 = l1.next if not l1.next is None else ListNode(0)
            l2 = l2.next if not l2.next is None else ListNode(0)
            final_node = final_node.next
            i += 1
        if carry != 0:
            final_node.next = ListNode(carry)
        return first_node_pointer


if __name__ == '__main__':
    l1 = ListNode(2)
    l2 = ListNode(5)
    l1.next = ListNode(4)
    l2.next = ListNode(6)
    l1.next.next = ListNode(3)
    l2.next.next = ListNode(4)
    solution = Solution()
    answer = solution.addTwoNumbers(l1, l2)
    while not answer is None:
        print(answer.val)
        answer = answer.next
    l3 = ListNode(9)
    l3.next = ListNode(9)
    l3.next.next = ListNode(9)
    l3.next.next.next = ListNode(9)
    l3.next.next.next.next = ListNode(9)
    l3.next.next.next.next.next = ListNode(9)
    l3.next.next.next.next.next.next = ListNode(9)
    l4 = ListNode(9)
    l4.next = ListNode(9)
    l4.next.next = ListNode(9)
    l4.next.next.next = ListNode(9)
    answer = solution.addTwoNumbers(l3, l4)
    while not answer is None:
        print(answer.val)
        answer = answer.next
