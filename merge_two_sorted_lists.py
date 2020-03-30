# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    n1 = l1
    n2 = l2
    tmp_list = []
    while n1 and n2:
        num1 = n1.val
        num2 = n2.val
        if num1 < num2:
            tmp_list.append(ListNode(num1))
            n1 = n1.next
        elif num2 < num1:
            tmp_list.append(ListNode(num2))
            n2 = n2.next
        elif num1 == num2:
            tmp_list.append(ListNode(num1))
            tmp_list.append(ListNode(num2))
            n1 = n1.next
            n2 = n2.next
    while n1:
        num1 = n1.val
        tmp_list.append(ListNode(num1))
        n1 = n1.next

    while n2:
        num2 = n2.val
        tmp_list.append(ListNode(num2))
        n2 = n2.next
    if len(tmp_list) > 0:
        l3 = tmp_list[0]
        node = l3
        for item in tmp_list[1:]:
            node.next = item
            node = item
        return l3
    else:
        return None


l1 = ListNode(0)
#l2 = ListNode(20)
#l3 = ListNode(30)
#l1.next = l2
#l2.next = l3

#l4 = ListNode()
#l5 = ListNode(20)
#l6 = ListNode(50)
#l4.next  = l5
#l5.next = l6


mergeTwoLists(l1, None)
