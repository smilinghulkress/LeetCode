# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd = head
        even = head.next
        evenHead = even
        prevOdd = odd

        while odd and even:
            if even:
                odd.next = even.next
                prevOdd = odd
                odd = odd.next
            if odd:
                even.next = odd.next
                even = even.next
        prevOdd.next = evenHead
        return head

def printLinkedList(h):
    ans = ''
    while(h):
        value = str(h.val)
        ans+= value +'->'
        h = h.next
    print(ans)

head =ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)
head.next = two
two.next = three
three.next = four
four.next = five
five.next = six
printLinkedList(head)
sol = Solution()
printLinkedList(sol.oddEvenList(head))